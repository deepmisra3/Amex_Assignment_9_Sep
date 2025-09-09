from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/weather")
async def get_weather(lat: float, lon: float):
    # Step 1: Get temperature from open-meteo
    try:
        async with httpx.AsyncClient() as client:
            weather_url = "https://api.open-meteo.com/v1/forecast"
            response = await client.get(weather_url, params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            })
            data = response.json()
            temperature = data["current_weather"]["temperature"]
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Weather API error: {e}"})

    # Step 2: Generate LLM-based report
    report = await generate_weather_report(lat, lon, temperature)

    # Step 3: Return response
    return {
        "latitude": lat,
        "longitude": lon,
        "temperature": temperature,
        "report": report
    }


async def generate_weather_report(lat: float, lon: float, temperature: float):
    try:
        async with httpx.AsyncClient() as client:
            headers = {
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "You are a helpful weather assistant."},
                    {"role": "user", "content": f"Generate a short, friendly weather report for:\nLatitude: {lat}, Longitude: {lon}, Temperature: {temperature}°C"}
                ],
                "max_tokens": 60
            }
            response = await client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            reply = response.json()
            return reply["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error generating report: {e}"

Weather-FastAPI Docker Setup Instructions

1) Install Docker Desktop
Ensure Docker Desktop is installed and running on your local system.
- Download the Docker Image
- Visit the following link:
https://drive.google.com/file/d/1RYs8Q-QMgx5IUezYWuZ1Wd4PNwtEeZli/view?usp=drive_link
- Download the file named weather-fastapi.tar.
- Place the File in Your Working Directory

2) Move weather-fastapi.tar to the folder where you'll run your Docker commands.
- Load the Docker Image

3) Open VS Code or PowerShell and run:
docker load -i weather-fastapi.tar
- Create a .env File with Your OpenAI API Key

4)Run the following command in PowerShell or VS Code:
echo "OPENAI_API_KEY=sk-..." > .env
- Replace sk-... with your actual OpenAI API key. You can generate one from:
https://platform.openai.com/api-keys
- Run the Docker Container Using the .env File
docker run -p 8000:8000 --env-file .env weather-fastapi
- Alternative Run Method (if .env doesn’t work)
You can pass the API key directly in the command:
docker run -p 8000:8000 -e OPENAI_API_KEY=YOUR_API_KEY weather-fastapi

- Replace YOUR_API_KEY with your actual OpenAI key generated from openai website.

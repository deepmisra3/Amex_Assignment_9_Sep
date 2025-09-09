async function getWeather() {
    const lat = document.getElementById("lat").value;
    const lon = document.getElementById("lon").value;

    const output = document.getElementById("output");
    output.innerHTML = "Loading...";

    try {
        const res = await fetch(`/weather?lat=${lat}&lon=${lon}`);
        const data = await res.json();

        if (res.ok) {
            output.innerHTML = `
                <p><strong>Latitude:</strong> ${data.latitude}</p>
                <p><strong>Longitude:</strong> ${data.longitude}</p>
                <p><strong>Temperature:</strong> ${data.temperature} °C</p>
                <p><strong>Report:</strong> ${data.report}</p>
            `;
        } else {
            output.innerHTML = `<p style="color:red;">${data.error}</p>`;
        }
    } catch (err) {
        output.innerHTML = `<p style="color:red;">Fetch error: ${err}</p>`;
    }
}

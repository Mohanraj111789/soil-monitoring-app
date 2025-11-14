async function updateDashboard() {
    try {
        const moisture = await getMoisture();
        const humidity = await getHumidity();
        const ldr = await getLDR();
        const water = await getWaterStatus();
        const mode = await getMode();
        const temperature = await getTemperature();

        document.getElementById("moistureValue").innerText = moisture.value + " %";
        document.getElementById("humidityValue").innerText = humidity.value + " %";
        document.getElementById("ldrValue").innerText = ldr.value;
        document.getElementById("waterStatus").innerText = water.status ? "Water Present" : "No Water";
        document.getElementById("modeStatus").innerText = mode.mode;
        document.getElementById("temperatureValue").innerText = temperature.value + " °C";


    } catch (e) {
        console.log("Error fetching data:", e);
    }
}

// Refresh every 2 seconds
setInterval(updateDashboard, 2000);
updateDashboard();

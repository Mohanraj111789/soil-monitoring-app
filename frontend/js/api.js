const API_BASE = "http://localhost:8000"; // change to your server IP

// ----- GET SENSOR VALUES -----
async function getMoisture() {
    return fetch(`${API_BASE}/sensor/moisture`).then(res => res.json());
}

async function getHumidity() {
    return fetch(`${API_BASE}/sensor/humidity`).then(res => res.json());
}

async function getLDR() {
    return fetch(`${API_BASE}/sensor/ldr`).then(res => res.json());
}

async function getWaterStatus() {
    return fetch(`${API_BASE}/sensor/water`).then(res => res.json());
}

async function getMode() {
    return fetch(`${API_BASE}/switch/mode`).then(res => res.json());
}

async function getTemperature() {
    return fetch(`${API_BASE}/sensor/temperature`).then(res => res.json());
}

async function getLDR() {
    return fetch(`${API_BASE}/sensor/ldr`).then(res => res.json());
}

// ----- UPDATE MODE -----
async function updateMode(mode) {
    return fetch(`${API_BASE}/switch/mode/${mode}`, {
        method: "POST"
    }).then(res => res.json());
}

// ----- MANUAL SWITCH -----
async function updateManualState(state) {
    return fetch(`${API_BASE}/switch/manual/${state}`, {
        method: "POST"
    }).then(res => res.json());
}

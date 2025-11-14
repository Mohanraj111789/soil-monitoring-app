from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.sensor_routes import router as sensor_router

app = FastAPI(
    title="Soil Monitoring API",
    description="Backend for IoT Soil Moisture Dashboard",
    version="1.0.0"
)

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(sensor_router)

@app.get("/")
def home():
    return {"message": "Soil Monitoring Backend Running!"}

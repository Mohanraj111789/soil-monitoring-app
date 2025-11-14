from fastapi import APIRouter
from services.sensor_service import (
    get_dummy_moisture,
    get_dummy_humidity,
    get_dummy_ldr,
    get_dummy_water_status,
    get_dummy_temperature,
    get_mode,
    set_mode,
    manual_switch
)

router = APIRouter(prefix="", tags=["Soil Monitoring API"])


# ------------ SENSOR ROUTES ------------

@router.get("/sensor/moisture")
def moisture():
    return {"value": get_dummy_moisture()}


@router.get("/sensor/humidity")
def humidity():
    return {"value": get_dummy_humidity()}

@router.get("/sensor/temperature")
def temperature():
    return {"value": get_dummy_temperature()}

@router.get("/sensor/ldr")
def ldr():
    return {"value": get_dummy_ldr()}


@router.get("/sensor/water")
def water_status():
    return {"status": get_dummy_water_status()}


# ------------ SWITCH ROUTES ------------

@router.get("/switch/mode")
def get_current_mode():
    return {"mode": get_mode()}


@router.post("/switch/mode/{mode}")
def update_mode(mode: str):
    return set_mode(mode)


@router.post("/switch/manual/{state}")
def update_manual_switch(state: str):
    return manual_switch(state)

from pydantic import BaseModel

class SensorValue(BaseModel):
    value: int

class WaterStatus(BaseModel):
    status: bool

class Mode(BaseModel):
    mode: str

class ManualSwitch(BaseModel):
    state: str

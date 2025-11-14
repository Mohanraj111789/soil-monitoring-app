import random

# Dummy stored variables
_current_mode = "auto"
_manual_state = "off"

def get_dummy_moisture():
    """Return random soil moisture percentage"""
    return random.randint(30, 90)

def get_dummy_humidity():
    """Return random humidity percentage"""
    return random.randint(40, 80)

def get_dummy_ldr():
    """Return random light intensity value"""
    return random.randint(100, 900)

def get_dummy_water_status():
    """Return dummy water presence True/False"""
    return random.choice([True, False])


# ---------------- Switch Logic ------------------

def get_mode():
    """Return the current device mode"""
    return _current_mode

def set_mode(mode: str):
    """Set mode to manual or auto"""
    global _current_mode
    if mode not in ["manual", "auto"]:
        return {"error": "Invalid mode"}
    _current_mode = mode
    return {"message": "Mode updated", "mode": _current_mode}

def manual_switch(state: str):
    """Turn pump ON/OFF in manual mode"""
    global _manual_state
    if state not in ["on", "off"]:
        return {"error": "Invalid state"}
    _manual_state = state
    return {"message": f"Pump turned {state}", "state": _manual_state}

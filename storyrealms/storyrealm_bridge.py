# storyrealms/storyrealm_bridge.py

import json
import os

# Simulated database for realm state
REALM_STATE_FILE = "storyrealms/realm_state.json"

def _load_realm_state():
    if not os.path.exists(REALM_STATE_FILE):
        return {"current_realm": None, "events": []}
    with open(REALM_STATE_FILE, "r") as f:
        return json.load(f)

def _save_realm_state(state):
    with open(REALM_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def enter_storyrealm(realm_name: str):
    state = _load_realm_state()
    state["current_realm"] = realm_name
    _save_realm_state(state)
    return {"status": "entered", "realm": realm_name}

def push_event_to_realm(event_data: dict):
    state = _load_realm_state()
    state.setdefault("events", []).append(event_data)
    _save_realm_state(state)
    return {"status": "event_pushed", "event": event_data}

def get_current_realm():
    state = _load_realm_state()
    return {"current_realm": state.get("current_realm")}

def list_realm_events():
    state = _load_realm_state()
    return {"events": state.get("events", [])}

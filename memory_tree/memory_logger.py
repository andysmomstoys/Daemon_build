
import json
from datetime import datetime

def log_event(event_type, content):
    memory = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "content": content
    }
    with open("memory_log.json", "a") as f:
        f.write(json.dumps(memory) + "\n")

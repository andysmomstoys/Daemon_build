# memory_tree/memory_logger.py
import json
import os
from datetime import datetime

class MemoryLogger:
    def __init__(self, log_dir="memory_tree/logs"):
        os.makedirs(log_dir, exist_ok=True)
        self.log_file = os.path.join(log_dir, "memory_log.json")

    def log_event(self, event_type, content):
        timestamp = datetime.utcnow().isoformat()
        log_entry = {"timestamp": timestamp, "type": event_type, "content": content}
        self._append_log(log_entry)

    def _append_log(self, entry):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(entry)
        with open(self.log_file, "w") as f:
            json.dump(data, f, indent=2)

    def get_latest_events(self, count=5):
        if not os.path.exists(self.log_file):
            return []
        with open(self.log_file, "r") as f:
            data = json.load(f)
        return data[-count:]

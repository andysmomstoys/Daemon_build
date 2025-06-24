# guardian/self_reflector.py
import time
from codex.interface import CodexInterface
from optimizer.auto_upgrade import run_auto_optimization

class SelfReflector:
    def __init__(self):
        self.codex = CodexInterface()
        self.log = []

    def reflect_on_logs(self):
        recent_logs = self.codex.get_recent_logs(limit=10)
        for log in recent_logs:
            insight = self.analyze_log(log)
            self.log.append(insight)

    def analyze_log(self, log_entry):
        if "error" in log_entry.lower():
            return f"Insight: Detected issue — {log_entry}. Suggested refactor."
        if "success" in log_entry.lower():
            return f"Insight: Confirmed behavior — {log_entry}."
        return f"Observation: {log_entry}"

    def run_daily_reflection(self):
        while True:
            self.reflect_on_logs()
            run_auto_optimization()
            time.sleep(86400)  # Run once a day

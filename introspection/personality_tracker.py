import json
import datetime
from codex.ingestion import ingest_observation

class PersonalityTracker:
    def __init__(self, log_path="introspection/personality_log.json"):
        self.log_path = log_path
        self.current_traits = {}
        self.load()

    def load(self):
        try:
            with open(self.log_path, "r") as f:
                self.current_traits = json.load(f)
        except FileNotFoundError:
            self.current_traits = {}

    def log_trait_change(self, trait, value):
        timestamp = datetime.datetime.now().isoformat()
        entry = {"timestamp": timestamp, "trait": trait, "value": value}
        self.current_traits[trait] = value
        self._append_log(entry)

    def _append_log(self, entry):
        try:
            with open(self.log_path, "a") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"[PersonalityTracker] Error logging trait: {e}")

    def get_traits(self):
        return self.current_traits

    def log_state(self):
        timestamp = datetime.datetime.now().isoformat()
        state_snapshot = {
            "timestamp": timestamp,
            "current_traits": self.current_traits
        }
        print(f"[PersonalityTracker] Current state: {json.dumps(state_snapshot, indent=2)}")
        ingest_observation(f"Personality state logged: {json.dumps(self.current_traits)}")

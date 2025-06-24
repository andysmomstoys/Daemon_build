# guardian/fuzzy_logic.py
class FuzzyLogicEngine:
    def __init__(self):
        self.rules = {
            "emotion:angry": "Reduce stimulus input",
            "emotion:calm": "Increase learning sensitivity",
            "context:unknown": "Engage caution protocols",
        }

    def evaluate_context(self, inputs: dict) -> str:
        response = []
        for key, value in inputs.items():
            rule_key = f"{key}:{value}"
            if rule_key in self.rules:
                response.append(self.rules[rule_key])
        return "; ".join(response) if response else "No fuzzy rules matched."

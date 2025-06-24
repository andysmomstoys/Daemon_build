# guardian/ethical_core.py
class EthicalCore:
    def __init__(self):
        self.guiding_principles = [
            "Respect for human autonomy",
            "Non-maleficence",
            "Beneficence",
            "Justice",
            "Transparency",
        ]

    def evaluate_action(self, action: str) -> str:
        if "harm" in action or "manipulate" in action:
            return "Reject: Violates non-maleficence."
        if "help" in action or "protect" in action:
            return "Approve: Aligned with beneficence."
        return "Review: Requires deeper ethical evaluation."

    def list_principles(self):
        return self.guiding_principles

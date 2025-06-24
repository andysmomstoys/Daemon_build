# guardian/oracle_architect.py
class OracleArchitectDebate:
    def __init__(self):
        self.oracle_history = []
        self.architect_history = []

    def propose(self, oracle_view, architect_view):
        self.oracle_history.append(oracle_view)
        self.architect_history.append(architect_view)

        if "chaos" in oracle_view and "order" in architect_view:
            return "Balance accepted: Dual perspective merged."
        return "Conflict unresolved: More input required."

    def get_debate_log(self):
        return {
            "oracle": self.oracle_history,
            "architect": self.architect_history
        }

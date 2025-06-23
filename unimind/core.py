class Unimind:
    def __init__(self):
        self.thoughts = []
        self.state = {}
        self.history = []

    def register(self, key, value):
        self.state[key] = value

    def reflect(self, context):
        self.history.append(context)
        # Simple reasoning simulation
        if "conflict" in context:
            return "Initiate inner debate."
        return "Reflection logged."

    def pulse(self):
        return "🧠 Unimind active"

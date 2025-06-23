class Unimind:
    def __init__(self):
        self.modules = {
            "logic": [],
            "emotion": [],
            "memory": [],
            "ethics": [],
            "language": []
        }
        print("[Unimind] Core initialized.")

    def register(self, type, module):
        if type in self.modules:
            self.modules[type].append(module)
            print(f"[Unimind] Registered module under '{type}'")

    def reflect(self):
        print("[Unimind] Running reflection loop...")
        for logic_module in self.modules["logic"]:
            logic_module.think()

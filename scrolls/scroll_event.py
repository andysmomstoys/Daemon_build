# scrolls/scroll_event.py

class ScrollEvent:
    def __init__(self, name, trigger=None, action=None):
        self.name = name
        self.trigger = trigger  # Optional: function that returns True/False
        self.action = action    # Optional: function to run when triggered

    def check_trigger(self, input_data):
        if self.trigger:
            return self.trigger(input_data)
        return False

    def execute(self):
        if self.action:
            print(f"[ScrollEvent] Executing scroll: {self.name}")
            return self.action()
        else:
            print(f"[ScrollEvent] No action defined for {self.name}")

from collections import defaultdict

class TriggerManager:
    def __init__(self):
        self.trigger_counts = defaultdict(int)
        self.trigger_threshold = 3

    def track_input(self, input_text):
        for word in input_text.lower().split():
            self.trigger_counts[word] += 1
            if self.trigger_counts[word] >= self.trigger_threshold:
                return word
        return None

trigger_manager = TriggerManager()

def check_triggers(input_text):
    word = trigger_manager.track_input(input_text)
    if word:
        return f"Trigger reached for: {word}. Suggest studying topic."
    return None

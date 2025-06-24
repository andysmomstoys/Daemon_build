# scrolls/scroll_trigger.py

import time
from scrolls.scroll_engine import ScrollEngine

class ScrollTrigger:
    def __init__(self):
        self.scroll_engine = ScrollEngine()
        self.trigger_log = []

    def check_and_trigger(self, condition):
        """Check if a condition matches a known scroll trigger."""
        if condition == "optimize_self":
            self.scroll_engine.cast("optimize self")
            self.trigger_log.append(("optimize_self", time.time()))
        elif condition == "study_topic":
            self.scroll_engine.cast("study topic")
            self.trigger_log.append(("study_topic", time.time()))
        else:
            print(f"[ScrollTrigger] No scroll for condition: {condition}")

    def repeat_check(self, word_counts):
        for word, count in word_counts.items():
            if count >= 3:
                print(f"[ScrollTrigger] Triggering study of: {word}")
                self.scroll_engine.cast("study topic", topic=word)

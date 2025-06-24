# scrolls/scroll_engine.py
from scrolls.api_scrolls import execute_api_scroll
from scrolls.scroll_trigger import check_scroll_triggers
from scrolls.trigger_manager import check_triggers

class ScrollEngine:
    def __init__(self):
        # Built-in scrolls
        self.scrolls = {
            "optimize self": self._optimize_self,
            "study topic": self._study_topic,
            "trigger api scroll": execute_api_scroll
        }
        # Dynamically registered scrolls
        self.active_scrolls = []

    # Built-in scrolls
    def invoke(self, name, *args, **kwargs):
        if name in self.scrolls:
            return self.scrolls[name](*args, **kwargs)
        else:
            return self.invoke_dynamic_scroll(name)

    def _optimize_self(self):
        from optimizer.auto_upgrade import run_self_optimization
        return run_self_optimization()

    def _study_topic(self, topic):
        from codex.ingestion import ingest_observation
        content = f"Scroll triggered self-study of topic: {topic}"
        ingest_observation(content)
        return content

    def evaluate_triggers(self, input_text):
        return check_triggers(input_text)

    # Dynamic scrolls
    def register_scroll(self, scroll):
        if scroll not in self.active_scrolls:
            self.active_scrolls.append(scroll)
            print(f"[ScrollEngine] Registered scroll: {scroll['name']}")

    def invoke_dynamic_scroll(self, name):
        scroll = next((s for s in self.active_scrolls if s['name'] == name), None)
        if scroll:
            print(f"[ScrollEngine] Invoking dynamic scroll: {name}")
            return scroll['action']()
        else:
            raise ValueError(f"[ScrollEngine] Scroll not found: {name}")

    def monitor_scrolls(self):
        check_scroll_triggers(self.active_scrolls)

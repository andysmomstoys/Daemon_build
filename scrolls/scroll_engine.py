from scrolls.api_scrolls import execute_api_scroll
from scrolls.trigger_manager import check_triggers

class ScrollEngine:
    def __init__(self):
        self.scrolls = {
            "optimize self": self._optimize_self,
            "study topic": self._study_topic,
            "trigger api scroll": execute_api_scroll
        }

    def invoke(self, name, *args, **kwargs):
        if name in self.scrolls:
            return self.scrolls[name](*args, **kwargs)
        else:
            raise ValueError(f"[ScrollEngine] Unknown scroll: {name}")

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

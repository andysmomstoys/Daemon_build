# rituals/ritual_registry.py

from scrolls.scroll_engine import ScrollEngine

class RitualRegistry:
    def __init__(self):
        self.scroll_engine = ScrollEngine()
        self.registered_rituals = {
            "optimize self": self.cast_optimize_self,
            "summon knowledge": self.cast_codex_query
        }

    def cast_ritual(self, ritual_name: str, context: dict = {}):
        if ritual_name in self.registered_rituals:
            return self.registered_rituals[ritual_name](context)
        else:
            return f"Unknown ritual: {ritual_name}"

    def cast_optimize_self(self, context):
        return self.scroll_engine.cast_scroll("optimize self", context)

    def cast_codex_query(self, context):
        return self.scroll_engine.cast_scroll("summon scroll summary", context)

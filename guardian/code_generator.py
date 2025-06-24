# guardian/code_generator.py
import random

class CodeGenerator:
    def __init__(self):
        self.templates = {
            "python": "def {name}():\n    return {value}",
            "rust": "fn {name}() -> {typ} {{ {value} }}",
            "julia": "{name}() = {value}"
        }

    def generate(self, language, name, value, typ="Int"):
        if language not in self.templates:
            raise ValueError(f"Unsupported language: {language}")
        template = self.templates[language]
        return template.format(name=name, value=value, typ=typ)

    def random_test(self):
        lang = random.choice(list(self.templates.keys()))
        return self.generate(lang, "test_fn", "42")

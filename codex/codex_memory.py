from codex.parser import parse_codex_entry

class CodexMemory:
    def __init__(self):
        self.entries = []

    def add_entry(self, raw_text):
        entry = parse_codex_entry(raw_text)
        self.entries.append(entry)

    def search(self, keyword):
        return [e for e in self.entries if keyword.lower() in e["summary"].lower() or keyword.lower() in e["title"].lower()]

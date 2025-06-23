import os
from datetime import datetime

class ReflectionJournal:
    def __init__(self, journal_dir="introspection/journal_entries"):
        os.makedirs(journal_dir, exist_ok=True)
        self.journal_dir = journal_dir

    def write_entry(self, title, content):
        filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{title.replace(' ', '_')}.md"
        path = os.path.join(self.journal_dir, filename)
        with open(path, "w") as f:
            f.write(f"# {title}\n\n")
            f.write(content)
        return path

    def list_entries(self):
        return os.listdir(self.journal_dir)

    def read_entry(self, filename):
        path = os.path.join(self.journal_dir, filename)
        with open(path, "r") as f:
            return f.read()

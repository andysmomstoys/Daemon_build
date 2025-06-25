import os
import json

class CodexIngestion:
    def __init__(self):
        self.knowledge_base = {}

    def ingest_file(self, path):
        if path.endswith(".json"):
            with open(path, "r") as f:
                data = json.load(f)
                self.knowledge_base[path] = data
                print(f"[Codex] Loaded JSON file: {path}")
        elif path.endswith(".txt"):
            with open(path, "r") as f:
                self.knowledge_base[path] = f.read()
                print(f"[Codex] Loaded text file: {path}")
        else:
            print(f"[Codex] Unsupported file type: {path}")

    def summarize(self, path):
        if path in self.knowledge_base:
            content = self.knowledge_base[path]
            if isinstance(content, dict):
                return {k: str(v)[:50] for k, v in content.items()}
            return content[:250]
        else:
            return "[Codex] No data available for that path."

def ingest_documents(folder_path):
    ingestor = CodexIngestion()
    for file in os.listdir(folder_path):
        ingestor.ingest_file(os.path.join(folder_path, file))

def ingest_observation(content):
    """
    Simulates ingestion of external content into the Codex system.
    Logs or processes content for knowledge storage or symbolic study.
    """
    print(f"[Codex] Ingested content: {content}")
    return f"Codex acknowledged: {content}"

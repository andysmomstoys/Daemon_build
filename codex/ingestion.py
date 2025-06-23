import os
import glob

class CodexIngestor:
    @staticmethod
    def load_documents(path="./codex_library"):
        docs = []
        if os.path.exists(path):
            for file in glob.glob(f"{path}/*.txt"):
                with open(file, 'r') as f:
                    docs.append(f.read())
        print(f"📘 Loaded {len(docs)} Codex documents.")
        return docs

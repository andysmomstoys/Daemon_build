# memory_tree/semantic_index.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

class SemanticMemoryIndex:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.index = FAISS.from_texts([], self.embeddings)

    def add_memory(self, text, metadata=None):
        self.index.add_texts([text], metadatas=[metadata] if metadata else None)

    def query(self, text, k=3):
        results = self.index.similarity_search(text, k=k)
        return results

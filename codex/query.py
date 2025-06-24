# codex/query.py
from codex.ingestion import vector_store

def search_codex(query, top_k=5):
    print(f"[Codex] Searching for: {query}")
    results = vector_store.similarity_search(query, k=top_k)
    return [doc.page_content for doc in results]

def summarize_results(results):
    summary = "\n---\n".join(results[:3])  # simple summarizer
    return f"[SUMMARY]\n{summary}"

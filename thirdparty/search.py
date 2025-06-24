import requests

def web_search(query):
    """Perform a web search using DuckDuckGo Lite"""
    url = f"https://lite.duckduckgo.com/lite/?q={query}"
    print(f"[WebSearch] Search URL: {url}")
    return url  # In production, you'd parse HTML or use an API

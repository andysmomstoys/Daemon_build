import requests

def fetch_latest_news(topic="technology"):
    """Fetch headlines from a news API"""
    url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey=YOUR_NEWSAPI_KEY"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [article["title"] for article in articles][:5]
    else:
        print(f"[NewsAPI] Failed to fetch news: {response.status_code}")
        return []

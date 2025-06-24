# scrolls/api_scrolls.py
import requests

def fetch_weather(city):
    response = requests.get(f"https://wttr.in/{city}?format=3")
    return response.text

def get_news_headlines(api_key, topic="technology"):
    url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey={api_key}"
    res = requests.get(url)
    if res.status_code == 200:
        headlines = [article['title'] for article in res.json().get('articles', [])]
        return headlines
    return []

def scroll_invoke_weather(city):
    print(f"[SCROLL] Weather Ritual: {fetch_weather(city)}")

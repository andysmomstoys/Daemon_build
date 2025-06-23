# scrolls/api_scrolls.py

import requests
from codex.ingestion import ingest_external_summary

def fetch_weather(context):
    location = context.get("location", "Denver")
    response = requests.get(f"https://wttr.in/{location}?format=3")
    return response.text

def fetch_news(context):
    response = requests.get("https://api.currentsapi.services/v1/latest-news", headers={
        "Authorization": context.get("news_api_key", "demo-key")
    })
    data = response.json()
    return data.get("news", [])[:3]

def summarize_url(context):
    url = context.get("url")
    if not url:
        return "No URL provided."
    return ingest_external_summary(url)

available_scrolls = {
    "weather forecast": fetch_weather,
    "latest news": fetch_news,
    "summon scroll summary": summarize_url
}

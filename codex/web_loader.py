import requests
from bs4 import BeautifulSoup

def fetch_and_clean_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return "\n".join(p.get_text() for p in paragraphs if p.get_text())

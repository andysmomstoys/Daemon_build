import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        "location": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"]
    } if response.status_code == 200 else {"error": "Weather data unavailable"}

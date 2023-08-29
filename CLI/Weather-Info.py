import requests
import json
from datetime import datetime

WEATHER_API_URL = "https://wttr.in/?format=j1"

def fetch_weather_data():
    try:
        response = requests.get(WEATHER_API_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred while fetching weather data:", e)
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", e)

def parse_weather_data(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        print("Error occurred while parsing weather data:", e)

def get_weather_symbol(weather_code):
    symbols = {
        "113": "☀️",  # Clear/Sunny
        "116": "☁️",  # Partly cloudy
        "119": "☁️",  # Cloudy
        "122": "🌦️",  # Overcast
        "143": "🌫️",  # Mist
        "176": "🌧️",  # Patchy rain possible
        "179": "🌧️",  # Patchy snow possible
        "182": "🌧️",  # Patchy sleet possible
        "185": "🌧️",  # Patchy freezing drizzle possible
        "200": "🌧️",  # Thundery outbreaks possible
        "227": "🌨️",  # Blowing snow
        "230": "🌨️",  # Blizzard
        "248": "🌫️",  # Fog
        "260": "🌫️",  # Freezing fog
        "263": "🌧️",  # Patchy light drizzle
        "266": "🌧️",  # Light drizzle
        "281": "🌧️",  # Freezing drizzle
        "284": "🌧️",  # Heavy freezing drizzle
        "293": "🌧️",  # Patchy light rain
        "296": "🌧️",  # Light rain
        "299": "🌧️",  # Moderate rain at times
        "302": "🌧️",  # Moderate rain
        "305": "🌧️",  # Heavy rain at times
        "308": "🌧️",  # Heavy rain
        "311": "🌧️",  # Light freezing rain
        "314": "🌧️",  # Moderate or heavy freezing rain
        "317": "🌧️",  # Light sleet
        "320": "🌧️",  # Moderate or heavy sleet
        "323": "🌨️",  # Patchy light snow
        "326": "🌨️",  # Light snow
        "329": "❄️",  # Patchy moderate snow
        "332": "❄️",  # Moderate snow
        "335": "❄️",  # Patchy heavy snow
        "338": "❄️",  # Heavy snow
        "350": "🌧️",  # Ice pellets
        "353": "🌧️",  # Light rain shower
        "356": "🌧️",  # Moderate or heavy rain shower
        "359": "🌧️",  # Torrential rain shower
        "362": "🌨️",  # Light sleet showers
        "365": "🌨️",  # Moderate or heavy sleet showers
        "368": "🌨️",  # Light snow showers
        "371": "❄️",  # Moderate or heavy snow showers
        "374": "🌧️",  # Light showers of ice pellets
        "377": "🌧️",  # Moderate or heavy showers of ice pellets
        "386": "⛈️",  # Patchy light rain in area with thunder
        "389": "⛈️",  # Moderate or heavy rain in area with thunder
        "392": "⛈️",  # Patchy light snow in area with thunder
        "395": "❄️",  # Moderate or heavy snow in area with thunder
    }
    return symbols.get(weather_code, "")

def display_current_weather(weather_data):
    try:
        location = weather_data["nearest_area"][0]["areaName"][0]["value"]
        current_condition = weather_data["current_condition"][0]["weatherDesc"][0]["value"]
        current_condition_code = weather_data["current_condition"][0].get("weatherCode", "")
        current_temp_c = weather_data["current_condition"][0].get("temp_C", "")
        current_temp_f = weather_data["current_condition"][0].get("temp_F", "")

        current_time = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

        print(f": - Weather in {location} - :")
        print(f"•    Current Time: {current_time}")
        print(f"•    Current Condition: {get_weather_symbol(current_condition_code)}  - {current_condition}")
        print(f"•    Current Temperature: {current_temp_f}°F -> ({current_temp_c}°C)")
        print("")
    except KeyError as e:
        print("Error occurred while displaying current weather:", e)

def display_forecast(weather_data):
    try:
        forecast = weather_data["weather"]
        print(": - Upcoming Forecast(s) - :")
        for day in forecast[:3]:  # Display forecast for the next 3 days
            date = day["date"]
            min_temp_c = day["mintempC"]
            max_temp_c = day["maxtempC"]
            min_temp_f = day["mintempF"]
            max_temp_f = day["maxtempF"]
            condition = day["hourly"][0]["weatherDesc"][0]["value"]
            condition_code = day["hourly"][0].get("weatherCode", "")

            print(f"•    Date: {date}")
            print(f"•    Condition: {get_weather_symbol(condition_code)}  - {condition}")
            print(f"•    Temperature: {min_temp_f}°F - {max_temp_f}°F -> ({min_temp_c}°C - {max_temp_c}°C)")
            print("")
    except KeyError as e:
        print("Error occurred while displaying forecast:", e)

def display_weather_info():
    weather_data = parse_weather_data(fetch_weather_data())
    if weather_data:
        display_current_weather(weather_data)
        display_forecast(weather_data)

display_weather_info()

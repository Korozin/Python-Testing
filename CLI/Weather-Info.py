import requests
import json

def get_location_info():
    url = "https://freegeoip.app/json/"
    response = requests.get(url)
    location_data = json.loads(response.text)
    location_name = f"{location_data['city']}, {location_data['region_code']}"
    return location_data, location_name

def get_weather_info():
    location_data, location_name = get_location_info()
    lat = location_data['latitude']
    lon = location_data['longitude']
    url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(url)
    data = json.loads(response.text)
    forecast_url = data['properties']['forecast']
    response = requests.get(forecast_url)
    forecast_data = json.loads(response.text)
    return forecast_data, location_name

def print_weather_info():
    forecast_data, location_name = get_weather_info()
    periods = forecast_data['properties']['periods']
    current_period = periods[0]
    temperature = current_period['temperature']
    description = current_period['detailedForecast']
    print(f"Weather information for {location_name} (approximated location):")
    print(f"Temperature: {temperature}°F")
    print(f"Description: {description}")

print_weather_info()

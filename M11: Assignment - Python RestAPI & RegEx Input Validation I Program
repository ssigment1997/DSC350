import re
import requests

API_KEY = "906b6939735602a519447e37a839d229"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Regex for US ZIP codes: 5 digits or 5 digits + hyphen + 4 digits
ZIP_REGEX = r"^\d{5}(-\d{4})?$"

def is_valid_zip(zip_code):
    return re.match(ZIP_REGEX, zip_code) is not None

def get_weather(zip_code):
    params = {
        "zip": f"{zip_code},us",
        "appid": API_KEY,
        "units": "imperial"  # Fahrenheit; use 'metric' for Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        city = data.get("name")
        weather = data.get("weather", [{}])[0].get("description", "N/A")
        temp = data.get("main", {}).get("temp", "N/A")
        print(f"\nWeather for {city} ({zip_code}):")
        print(f"  Condition: {weather.capitalize()}")
        print(f"  Temperature: {temp} °F\n")
    else:
        print("\nCould not retrieve weather data. Please check the zip code and try again.\n")

def main():
    while True:
        zip_code = input("Enter your US zip code (or 'q' to quit): ").strip()
        if zip_code.lower() == 'q':
            print("Goodbye!")
            break
        if not is_valid_zip(zip_code):
            print("Invalid zip code format. Please enter a valid US zip code (e.g., 12345 or 12345-6789).\n")
            continue
        get_weather(zip_code)

if __name__ == "__main__":
    main()

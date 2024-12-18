import requests


def get_weather_info(city):
    API_key = "8f38d38d94368d6eea4ff8d2d04f1860"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city.capitalize()}&appid={API_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        weather_info = {
            "temp": weather_data["main"]["temp"],
            "humidity": weather_data["main"]["humidity"],
            "pressure": weather_data["main"]["pressure"],
            "wind": weather_data["wind"]["speed"],
            "description": weather_data["weather"][0]["description"]
        }
        return weather_info
    else:
        return None

city = input("Enter City: ")
weather_info = get_weather_info(city)

def result_weather():
    if weather_info:
        print("Temperature:", round(weather_info["temp"] - 273.15, 2), "°C")
        print("Wind:", weather_info["wind"])
        print("Pressure:", weather_info["pressure"])
        print("Humidity:", weather_info["humidity"])
        print("Description:", weather_info["description"])

result_weather()
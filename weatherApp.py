import requests
import tkinter


city = input("Enter City: ")

API_key = "8f38d38d94368d6eea4ff8d2d04f1860"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city.capitalize()}&appid={API_key}"

response = requests.get(url)
data = response.json()

humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
wind = data["wind"]["speed"]
description = data["weather"][0]["description"]
temperature = data["main"]["temp"]

print("Temperature: ", round(temperature - 273.15, 2), "°C")
print("Wind: ", wind)
print("Pressure: ", pressure)
print("Humidity: ", humidity)
print("Description: ", description)

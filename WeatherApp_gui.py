import requests
from tkinter import *

#Screen
window = Tk()
window.title("Best Weather App")
window.minsize(width=400, height=350)
window.config(padx=20,pady=20)

#UI
location_label = Label(text="Enter Location")
location_label.pack(pady=5)

location_entry = Entry(width=20)
location_entry.pack(pady=5)

result_label = Label()
result_label.pack(pady=5)

temp_label = Label()
temp_label.pack(pady=5)

desc_label = Label()
desc_label.pack(pady=5)

wind_label = Label()
wind_label.pack(pady=5)

pres_label = Label()
pres_label.pack(pady=5)

humidity_label = Label()
humidity_label.pack(pady=5)

#Function to get weather data
def get_weather_info(city):
    API_key = "8f38d38d94368d6eea4ff8d2d04f1860"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city.capitalize()}&appid={API_key}" #after last } &units=metric can be addable to make kelvin to celcius convert automatically
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

#Function to connect button
def button_clicked():

    if location_entry.get() == "":
        result_label.config(text="Please enter location!")
        clear_labels()

    else:
        try:
            city = location_entry.get()
            weather_info = get_weather_info(city)
            result_label.config(text=f"Weather in {city.capitalize()}:")
            temp_label.config(text=f"Temperature: {round(weather_info["temp"] - 273.15, 2)} °C")
            desc_label.config(text=f"Description: {weather_info["description"].capitalize()}")
            wind_label.config(text=f"Wind: {weather_info["wind"]} m/s")
            pres_label.config(text=f"Pressure: {weather_info["pressure"]} hPa")
            humidity_label.config(text=f"Humidity: {weather_info["humidity"]}%")
        except (TypeError, KeyError):
            result_label.config(text="City not Found or API error.")
            clear_labels()

def clear_labels():
    temp_label.config(text="")
    desc_label.config(text="")
    wind_label.config(text="")
    pres_label.config(text="")
    humidity_label.config(text="")



location_button = Button(text="Learn the weather",command=button_clicked)
location_button.pack()


window.mainloop()
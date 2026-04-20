import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        data = response.json()

        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        humidity = data["current_condition"][0]["humidity"]

        print("\n📍 City:", city.title())
        print("🌡 Temperature:", temp, "°C")
        print("☁ Condition:", desc)
        print("💧 Humidity:", humidity)

        # -*- coding: utf-8 -*-
        with open("weather_report.txt", "a") as file:
            file.write(f"\nWeather Report for: {city.title()}\n")
            file.write(f"Temperature : {temp} C\n")
            file.write(f"Condition   : {desc}\n")
            file.write(f"Humidity    : {humidity}\n")
            file.write("-" * 30 + "\n")
            
    except Exception as e:
        print("Error:", e)

while True:
    city = input("\nEnter city name (or exit): ")

    if city.lower() == "exit":
        break

    get_weather(city)


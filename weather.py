import requests

try:

    city = input("Enter city name: ")

    response = requests.get(
        f"https://wttr.in/{city}?format=j1"
    )

    data = response.json()

    print("\n--- WEATHER REPORT ---")

    print(
        "City:",
        city
    )

    print(
        "Temperature:",
        data["current_condition"][0]["temp_C"],
        "°C"
    )

    print(
        "Weather:",
        data["current_condition"][0]["weatherDesc"][0]["value"]
    )

    print(
        "Humidity:",
        data["current_condition"][0]["humidity"]
    )

    print(
        "Wind Speed : ",
        data["current_condition"][0]["windspeedKmph"],
        "km/h"
    )

except:

    print("Weather data not found")
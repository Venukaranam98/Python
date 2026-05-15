import requests
import logging
import json

logging.basicConfig(level=logging.INFO)


weather_history = []


while True:

    print("\n--- WEATHER APP ---")

    print("1. Check Weather")

    print("2. View Search History")

    print("3. Save History")

    print("4. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        try:

            city = input("Enter city name: ")

            response = requests.get(
                f"https://wttr.in/{city}?format=j1"
            )

            if response.status_code == 200:

                data = response.json()

                logging.info(
                    "Weather data fetched successfully"
                )

                weather = {
                    "city": city,
                    "temperature":
                    data["current_condition"][0]["temp_C"],
                    "condition":
                    data["current_condition"][0]
                    ["weatherDesc"][0]["value"],
                    "humidity":
                    data["current_condition"][0]["humidity"],
                    "wind_speed":
                    data["current_condition"][0]
                    ["windspeedKmph"]
                }

                weather_history.append(weather)

                print("\n--- WEATHER REPORT ---")

                print("City:", weather["city"])

                print(
                    "Temperature:",
                    weather["temperature"],
                    "°C"
                )

                print(
                    "Weather:",
                    weather["condition"]
                )

                print(
                    "Humidity:",
                    weather["humidity"]
                )

                print(
                    "Wind Speed:",
                    weather["wind_speed"],
                    "km/h"
                )

            else:

                logging.warning(
                    "API returned warning status"
                )

        except:

            logging.error(
                "Failed to fetch weather data"
            )


    elif choice == "2":

        print("\n--- SEARCH HISTORY ---")

        for item in weather_history:

            print(
                item["city"],
                "-",
                item["temperature"],
                "°C"
            )


    elif choice == "3":

        with open("weather_history.json", "w") as file:

            json.dump(weather_history, file)

        print("History saved")


    elif choice == "4":

        print("Program closed")

        break


    else:

        print("Invalid choice")
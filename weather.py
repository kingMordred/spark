# import required modules
import requests

# Enter your API key here
api_key = "c230e7dd11396fa8e4f57efe79086a9f"

# base_url variable to store URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = "Tunis"

# Complete URL to store the complete URL address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
print(complete_url)

# Send a GET request to the API
response = requests.get(complete_url)

# Parse response JSON if request is successful
if response.status_code == 200:
    data = response.json()

    # Check if the city is found
    if data.get("cod") != "404":
        # Access weather information
        main_info = data.get("main")
        temperature = main_info.get("temp")
        pressure = main_info.get("pressure")
        humidity = main_info.get("humidity")
        weather = data.get("weather")
        description = weather[0].get("description")

        # Print weather details
        print("Temperature (in Kelvin): " + str(temperature))
        print("Atmospheric pressure (in hPa): " + str(pressure))
        print("Humidity (in percentage): " + str(humidity))
        print("Description: " + description)
    else:
        print("City Not Found")
else:
    print("Error occurred while retrieving weather data. Please try again.")

from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv() # loads the .env file

def get_current_weather(city="Madison, US"):
    # https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('OPENWEATHER_API_KEY')}
    # > URL that the program will use to make the request. 
    # > {os.getenv('OPENWEATHER_API_KEY')}: The API key that the program will use to authenticate
    #       with the OpenWeather API grabbed from .env file.
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('OPENWEATHER_API_KEY')}&q={city}&units=imperial"
    
    # Grabs the weather from the OpenWather API and stores it in the weather_data variable. 
    # Converts it to JavaScript Object Notation (JSON).
    weather_data = requests.get(request_url).json()
    
    return weather_data # returns the weather data

# Checks whether the script is being run directly or being imported. If ran directly, 
# it will ask for a city name and provide the weather data in the terminal.
if __name__ == "__main__": 
    print('\n*** Get Current Weather Conditions ** \n')
    city = input("Please enter a city name: ") # asks for the city name
    weather_data = get_current_weather(city) # calls the get_current_weather function to store the weather data
    print() 
    pprint(weather_data) # provide the weather data in the terminal
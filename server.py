from flask import Flask, render_template, request # Imports necessary components from Flask, function to render HTML templates, and handle incoming data
from weather import get_current_weather # Import function from weather.py
from waitress import serve # Helps serve our application on the web by importing the 'serve' function. Manages multiple simultaneous HTTP request more efficiently than the Flask development server, 

app = Flask(__name__) # Creates a Flask app

@app.route('/') # Accesses the root URL (homepage)
@app.route('/index')

def index():
    return render_template('index.html') # Renders the index.html template

@app.route('/weather') # Accesses the /weather URL
def get_weather():
    city = request.args.get('city') # Get the city from the URL
    weather_data = get_current_weather(city) # Get the weather data for the city
    return render_template( # Render the weather.html template with the weather data
        'weather.html', 
        # Sets various variables that weather.html will use 
        title = weather_data["name"], 
        status = weather_data["weather"][0]["description"].capitalize(), # Because "weather" is a list, we need to access the first element
        temp=f"{weather_data['main']['temp']:.1f}", # .1f rounds the temperature to one decimal place
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000) # Runs the app locally on port 8000
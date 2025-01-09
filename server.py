from flask import Flask, render_template, request 
from weather import get_current_weather # import function from weather.py
from waitress import serve # helps serve our application on the web

app = Flask(__name__) # creates a Flask app

@app.route('/') # accesses the root URL (homepage)
@app.route('/index')

def index():
    return render_template('index.html') # renders the index.html template

@app.route('/weather') # accesses the /weather URL
def get_weather():
    city = request.args.get('city') # get the city from the URL
    weather_data = get_current_weather(city) # get the weather data for the city
    return render_template( # render the weather.html template with the weather data
        'weather.html', 
        # sets various variables that weather.html will use 
        title = weather_data["name"], 
        status = weather_data["weather"][0]["description"].capitalize(), # because "weather" is a list, we need to access the first element
        temp=f"{weather_data['main']['temp']:.1f}", # .1f rounds the temperature to one decimal place
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000) # runs the app locally on port 8000
# app.py (Flask application)
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '246277edd7908d5f3418f78876038eb9'
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        return render_template('weather.html', city=city, temperature=temperature, description=description, icon=icon)
    else:
        return render_template('error.html')

def get_weather_data(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)

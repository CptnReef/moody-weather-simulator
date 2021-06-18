import os
import math
import requests
from tkinter import *
from flask import *

app = Flask(__name__)

@app.route("/home")
def home(state='Florida'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={state},Us&appid=a485168e9cae605b5d907b11ec1a547a'
    response = requests.get(url).json()
    temp = response['main']['temp']
    feels_like = response['main']['feels_like']

    mood = {
        'temp': math.floor((temp * 1.8) - 459.67), #convert to degrees
        'feels_like': math.floor((feels_like * 1.8) - 459.67), #convert to degrees
        'humidity': response['main']['humidity']
    }

    return render_template('index.html', mood=mood, state=state)

# weather = get_weather(API_KEY, city_name)

# print(weather['temp'],weather['feels_like'],weather['humidity'])

if __name__ == "__main__":
    app.run(debug=True)
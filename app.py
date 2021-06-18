import os
import math
import requests
from tkinter import *
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<state>")
def home(state):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={state},Us&appid=a485168e9cae605b5d907b11ec1a547a'
    response = requests.get(url).json()
    mood = {
        'response' : response,
        'math': math.floor #convert to degrees
        # 'feels_like': math.floor((feels_like * 1.8) - 459.67), #convert to degrees
        # 'humidity': response['main']['humidity']
    }
    return render_template("index.html", **mood)

if __name__ == "__main__":
    app.run(debug=True)
    
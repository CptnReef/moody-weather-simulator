import os
import math
from flask.helpers import url_for
import requests
from tkinter import *
from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def Home(state='California'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={state},Us&appid=a485168e9cae605b5d907b11ec1a547a'
    mood = {
        'response': requests.get(url).json(),
        'place': state,
        'math': math.floor,
        'mad_maffs': range(0,120)
    }

    return render_template('index.html', **mood)

@app.route("/<state>", methods=["GET", "POST"])
def weather(state='California'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={state},Us&appid=a485168e9cae605b5d907b11ec1a547a'
    mood = {
        'response': requests.get(url).json(),
        'place': state,
        'math': math.floor,
        'mad_maffs': range(0,120)
    }

    return render_template('index.html', **mood)


if __name__ == "__main__":
    app.run(debug=True)
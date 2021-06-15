import os
import math
import requests
from tkinter import *
from flask import Flask, redirect, url_for

city_name = 'Florida,Us'
API_KEY = 'a485168e9cae605b5d907b11ec1a547a'

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor((temp * 1.8) - 459.67) #convert to degrees

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67) #convert to degrees

    humidity = response['main']['humidity']


    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }

weather = get_weather(API_KEY, city_name)

print(weather['temp'],weather['feels_like'],weather['humidity'])
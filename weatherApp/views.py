from django.shortcuts import render
import datetime
import requests

# Create your views here.
def index(request):
    apikey = open("apikey, " "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
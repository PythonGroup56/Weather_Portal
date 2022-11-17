import requests

from django.shortcuts import render
from datetime import datetime

from .forms import CityForm


def index(request):
    form = CityForm()

    if request.method == 'POST':

        API_KEY = 'd01b7213b9978e719b3b055b3ecd7d2e'

        city_name = request.POST.get('name')
        print(request.POST)

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}'

        print(url)

        response_json = requests.get(url).json()

        current_time = datetime.now()

        formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")

        city_weather = {
            'city' : city_name,
            'temperature' : response_json ['main']['temp'],
            'description' : response_json ['weather'][0]['description'],
            'icon' : response_json ['weather'][0]['icon'],
            'time' : formatted_time,
            }

    else:
        city_weather = {}
    context = {
            'city_weather' : city_weather,
            'form' : form,
        }
    return render(request, 'weather_api/home.html', context)

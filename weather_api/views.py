import os
import requests
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render

from .forms import CityForm


def search(request):
    form = CityForm()
    city_weather = {}

    if request.method == "POST":

        API_KEY = os.getenv("API_KEY")
        city_name = request.POST.get("place")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}"

        response = requests.get(url)
    
        if response.ok == True:
            current_time = datetime.now()
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            response_json = response.json()
            city_weather = {
                "city": city_name,
                "temperature": response_json["main"]["temp"],
                "description": response_json["weather"][0]["description"],
                "icon": response_json["weather"][0]["icon"],
                "time": formatted_time,
            }
        else:
            messages.error(request, "Błędna nazwa miejsca!")
    context = {
        "city_weather": city_weather,
        "form": form,
    }
    return render(request, "weather_api/search_weather.html", context)

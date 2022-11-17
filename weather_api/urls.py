from django.urls import path

from . import views


urlpatterns = [
    path("weather_api/", views.index, name="weather_api"),
]
from django.urls import path

from . import views


urlpatterns = [
    path("search/", views.search, name="weather_api"),
]

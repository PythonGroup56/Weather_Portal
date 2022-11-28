from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("account/", views.account_profile, name="account"),
    path('change_password', views.change_password, name="change_password"),
    path("", views.home, name="home"),
]

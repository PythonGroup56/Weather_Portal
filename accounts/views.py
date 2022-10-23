from django.shortcuts import render, redirect
from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Udało się stworzyć konto - {user}")
            return redirect("login")

    context = {"form": form}
    return render(request, "registration_login/register.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Nazwa użytkownika lub hasło jest niepoprawne")

    context = {}
    return render(request, "registration_login/login.html", context)


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")

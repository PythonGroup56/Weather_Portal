from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.conf import settings

from .forms import CreateUserForm, ProfileForm, UserForm, ContactForm


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


@login_required(login_url="login")
def account_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Twoje konto zostało zaktulizowane")
            return redirect("account")

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "registration_login/account_settings.html", context)


def contact(request):
    form = ContactForm()
    if request.method == 'GET':
        context = {"form": form}
        return render(request, "registration_login/contact_page.html", context)

   
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            msg_name = form.cleaned_data.get('name')
            msg_email = form.cleaned_data.get('email')
            msg_message = form.cleaned_data.get('message')

        send_mail(
            f'Kontakt od użytkownika {msg_name}',
            f'Treść wiadomości: {msg_message}',
            msg_email,
            [settings.RECIPIENTS_LIST],
            fail_silently=False
        )

        return render(request, "registration_login/contact_page.html", {'msg_name': msg_name})
        

def home(request):
    context = {}
    return render(request, "registration_login/dashboard.html", context)

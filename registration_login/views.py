from django.shortcuts import render, redirect
from .forms import CreateUserForm

from django.contrib import messages



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Udało się stworzyć konto ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration_login/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'registration_login/login.html', context)
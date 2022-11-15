from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserForm(ModelForm):
    first_name = forms.CharField(max_length=64, required=True, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    last_name = forms.CharField(max_length=64, required=True, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"] 


class ProfileForm(ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    phone = forms.CharField(max_length=64, required=True, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    
    class Meta:
        model = Profile
        fields = ["profile_pic", "phone"]
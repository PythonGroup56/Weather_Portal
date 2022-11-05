from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64, null=True, help_text='Imię użytkownika')
    last_name = models.CharField(max_length=64, null=True, help_text='Nazwisko użytkownika')
    email = models.EmailField(null=True, help_text='E-mail użytkownika')
    profile_pic = models.ImageField(default="human_avatar.png",null=True, blank=True, help_text='Zdjęcie użytkownika')
    phone = models.CharField(max_length=64, help_text='Telefon użytkownika')
    date_registration = models.DateTimeField(auto_now_add=True, null=True, help_text='Data rejestracji')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default="human_avatar.png",
        upload_to="profile_pics",
        null=True,
        blank=True,
        help_text="Zdjęcie użytkownika",
    )
    phone = models.CharField(max_length=64, help_text="Telefon użytkownika")
    date_registration = models.DateTimeField(
        auto_now_add=True, null=True, help_text="Data rejestracji"
    )

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"

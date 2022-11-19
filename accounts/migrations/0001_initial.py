# Generated by Django 4.1.2 on 2022-11-05 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Imię użytkownika", max_length=64, null=True
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Nazwisko użytkownika", max_length=64, null=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="E-mail użytkownika", max_length=254, null=True
                    ),
                ),
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        default="human_avatar.png",
                        help_text="Zdjęcie użytkownika",
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "phone",
                    models.CharField(help_text="Telefon użytkownika", max_length=64),
                ),
                (
                    "date_registration",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Data rejestracji", null=True
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

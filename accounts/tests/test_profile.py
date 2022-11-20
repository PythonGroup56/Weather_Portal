from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from django.urls import reverse


def log_user(client):
    username = 'testowy'
    password = 'haslo1234'
    email = 'test@test.com'
    user = User.objects.create_user(username, password=password, email=email)
    client.login(username=username, password=password, email=email)
    return user

class TestUpdateProfile(TestCase):
    def test_create_profile(self):
        user = log_user(self.client)
        self.client.post(reverse('account'), {'first_name': 'jan', 'last_name': 'kowalski', 
        'email': 'test@test.com', 'phone': '+48123123123', 'profile_pic': 'human_avatar.png'})
        user.refresh_from_db()
        profile: Profile = user.profile

        
        self.assertEqual(user.first_name, 'jan')
        self.assertEqual(user.last_name, 'kowalski')
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(profile.phone, '+48123123123')
        self.assertEqual(profile.profile_pic, 'human_avatar.png')

   






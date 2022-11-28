from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from django.urls import reverse


class TestModel(TestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.account_url = reverse("account")
        self.home_url = reverse("home")
        self.user = {
            "username": "john",
            "email": "john@john.com",
            "password1": "haslo1234",
            "password2": "haslo1234",
        }
        self.user_short_password = {
            "username": "john",
            "email": "john@john.com",
            "password1": "haslo",
            "password2": "haslo",
        }
        self.user_unmatch_password = {
            "username": "john",
            "email": "john@john.com",
            "password1": "abcd",
            "password2": "haslo",
        }
        self.user_invalid_email = {
            "username": "john",
            "email": "john@1",
            "password1": "haslo1234",
            "password2": "haslo1234",
        }

        return super().setUp()


class RegisterTest(TestModel):
    def test_sign_up_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration_login/register.html")

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user)
        self.assertEqual(response.status_code, 302)

    def test_no_register_user_with_short_password(self):
        response = self.client.post(self.register_url, self.user_short_password)
        self.assertEqual(response.status_code, 200)

    def test_no_register_user_with_unmatch_password(self):
        response = self.client.post(self.register_url, self.user_unmatch_password)
        self.assertEqual(response.status_code, 200)

    def test_no_register_user_with_invalid_email(self):
        response = self.client.post(self.register_url, self.user_invalid_email)
        self.assertEqual(response.status_code, 200)


class LoginTest(TestModel):
    def test_access_login_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration_login/login.html")

    def test_login_success(self):
        user = User.objects.create_user(
            username=self.user["username"],
            email=self.user["email"],
            password=self.user["password1"],
        )
        response = self.client.post(
            self.login_url,
            {"username": user.username, "password": self.user["password1"]},
        )
        self.assertEqual(response.status_code, 302)

    def test_no_login_with_invalid_username(self):
        user = User.objects.create_user(
            username=self.user["username"],
            email=self.user["email"],
            password=self.user["password1"],
        )
        response = self.client.post(
            self.login_url, {"password": self.user["password1"], "username": "invalid"}
        )
        self.assertEqual(response.status_code, 200)

    def test_no_login_with_no_password(self):
        user = User.objects.create_user(
            username=self.user["username"],
            email=self.user["email"],
            password=self.user["password1"],
        )
        response = self.client.post(
            self.login_url, {"username": user.username, "password": "invalid"}
        )
        self.assertEqual(response.status_code, 200)


class TestAccountProfile(TestModel):
    def test_profile_page(self):
        response = self.client.get(self.account_url)
        self.assertEqual(response.status_code, 302)


class TestHomePage(TestModel):
    def test_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration_login/dashboard.html")

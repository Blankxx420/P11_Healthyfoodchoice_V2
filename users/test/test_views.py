from django.test import TestCase, Client
from django.urls import reverse

from users.models import User


class TestUsersViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user1",
            email="user1@gmail.com",
            password="password1234",
        )
        self.account_url = reverse("account")
        self.register_url = reverse("register")

    def test_registration_success(self):
        data = {
            "username": "user1",
            "email": "user1@gmail.com",
            "password1": "password1234",
            "password2": "password1234",
        }

        self.client.post(self.register_url, data)
        self.assertEqual(User.objects.count(), 1)
        self.client.force_login(self.user)

    def test_account_page(self):
        # check that reverse the account template
        self.client.force_login(self.user)
        response = self.client.get(self.account_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/account.html")
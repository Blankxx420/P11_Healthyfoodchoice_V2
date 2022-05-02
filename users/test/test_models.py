from django.test import TestCase

from users.models import User


class ModelsTestCase(TestCase):
    def test_user_str(self):
        user = User.objects.create(
            email="user1@gmail.com",
            username="user1",
            password="password1234",
        )
        print(str(user))
        self.assertEqual(str(user), "user1@gmail.com")

    def test_superuser_is_admin(self):
        superuser = User.objects.create_superuser(
            email="superuser1@gmail.com",
            username="superuser1",
            password="password1234",
        )
        self.assertIs(superuser.is_admin, True)

    def test_user_not_admin(self):
        user = User.objects.create_user(
            email="user1@gmail.com",
            username="user1",
            password="password1234",
        )
        self.assertIs(user.is_admin, False)


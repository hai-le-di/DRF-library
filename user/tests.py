from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    def test_create_user(self):
        User = get_user_model()
        email = "test@example.com"
        password = "password123"
        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        email = "admin@example.com"
        password = "password123"
        admin_user = User.objects.create_superuser(email=email, password=password)
        self.assertEqual(admin_user.email, email)
        self.assertTrue(admin_user.check_password(password))
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(str(admin_user), email)

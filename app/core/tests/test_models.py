from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@caleb.com'
        password = 'abadasspass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@CALEB.COM'
        user = get_user_model().objects.create_user(email, 'abadasspass')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abadasspass')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@caleb.com',
            'abadasspass'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

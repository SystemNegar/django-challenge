from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import TestCase

from .common_functions import sample_user, sample_superuser


class UserModelTest(TestCase):
    def test_create_user_with_username_successful(self):
        """Test creating a new user with a username is successful"""
        username = 'username@ticketing.sample'
        password = 'password@123'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        self.assertEqual(user.username, username)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertTrue(user.check_password(password))

    def test_creating_user_with_none_username(self):
        """Test creating a new user with a none username"""
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(username=None, password='1234@passwor')

    def test_creating_user_with_invalid_username(self):
        """Test creating a new user with an invalid username"""
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(username='abcd 1234', password='1234@passwor')

    def test_creating_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            username='superuser@ticketing.sample',
            password='1234@password'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_new_user_with_duplicate_username_unsuccessful(self):
        """Test creating a new user with duplicate username is unsuccessful"""
        user = sample_user()
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_user(username=user.username, password='123@pass')

    def test_create_new_superuser_with_duplicate_username_unsuccessful(self):
        """Test creating a new superuser with duplicate username is unsuccessful"""
        user = sample_superuser()
        with self.assertRaises(ValidationError):
            get_user_model().objects.create_superuser(username=user.username, password='123@pass')

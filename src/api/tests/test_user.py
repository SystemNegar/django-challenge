from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from user_management.tests.common_functions import sample_superuser, sample_group, sample_user

from user_management.serializers import UserSerializer, PermissionSerializer, GroupSerializer

USERS_LIST_URL = reverse('api:user_management:users-list')


class PublicUsersAPITests(TestCase):
    """Test the public available users API"""
    def setUp(self) -> None:
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving permissions"""
        result = self.client.get(USERS_LIST_URL)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUsersAPITests(TestCase):
    """Test the authorized user users API"""
    def setUp(self) -> None:
        self.super_user = sample_superuser()
        self.client = APIClient()
        self.client.force_authenticate(self.super_user)

    def test_create_user_successful(self):
        """Test creating a new user is successful"""
        payload = {
            "password": "@strong#password",
            "is_superuser": False,
            "is_staff": False,
            "username": "sample_user@ticketing.sample",
            "is_active": True,
            "groups": [],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['username'], payload['username'])
        self.assertFalse(result.data['is_superuser'])
        self.assertTrue(result.data['is_active'])
        self.assertIsNone(result.data['last_login'])

    def test_create_user_with_group_successful(self):
        """Test creating a new user with group is successful"""
        group = sample_group()
        payload = {
            "password": "@strong#password",
            "is_superuser": False,
            "is_staff": False,
            "username": "sample_user@ticketing.sample",
            "is_active": True,
            "groups": [group.id],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['username'], payload['username'])
        self.assertEqual(result.data['groups'], GroupSerializer(many=True, instance=[group]).data)
        self.assertFalse(result.data['is_superuser'])
        self.assertTrue(result.data['is_active'])
        self.assertIsNone(result.data['last_login'])

    def test_create_user_with_permission_successful(self):
        """Test creating a new user with permission is successful"""
        permission = Permission.objects.get(pk=1)
        payload = {
            "password": "@strong#password",
            "is_superuser": False,
            "is_staff": False,
            "username": "sample_user@ticketing.sample",
            "is_active": True,
            "groups": [],
            "user_permissions": [permission.id]
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['username'], payload['username'])
        self.assertEqual(result.data['user_permissions'], PermissionSerializer(many=True, instance=[permission]).data)
        self.assertFalse(result.data['is_superuser'])
        self.assertTrue(result.data['is_active'])
        self.assertIsNone(result.data['last_login'])

    def test_create_user_with_group_with_permission_to_do_something_successful(self):
        """Test creating a new user with group with the permission to do something is successful"""
        group = sample_group()
        permission = Permission.objects.get(codename='add_group')
        group.permissions.set([permission.id])

        payload = {
            "password": "@strong#password",
            "is_superuser": False,
            "is_staff": False,
            "username": "sample_user@ticketing.sample",
            "is_active": True,
            "groups": [group.id],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['username'], payload['username'])
        self.assertEqual(result.data['groups'], GroupSerializer(many=True, instance=[group]).data)

        user = get_user_model().objects.get(pk=result.data['id'])
        self.assertTrue(user.has_perm("auth.add_group"))

        self.client.logout()
        self.client.force_authenticate(user=user)
        create_group_payload = {
            'name': 'Sample Group Two',
        }
        create_group_result = self.client.post(reverse('api:user_management:groups-list'), create_group_payload)
        self.assertEqual(create_group_result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(create_group_result.data['name'], create_group_payload['name'])

    def test_create_user_with_group_without_permission_to_do_something_unsuccessful(self):
        """Test creating a new user with group without the permission to do something is unsuccessful"""
        payload = {
            "password": "@strong#password",
            "is_superuser": False,
            "is_staff": False,
            "username": "sample_user@ticketing.sample",
            "is_active": True,
            "groups": [],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['username'], payload['username'])

        user = get_user_model().objects.get(pk=result.data['id'])
        self.assertFalse(user.has_perm("auth.add_group"))

        self.client.logout()
        self.client.force_authenticate(user=user)
        create_group_payload = {
            'name': 'Sample Group Two',
        }
        create_group_result = self.client.post(reverse('api:user_management:groups-list'), create_group_payload)
        self.assertEqual(create_group_result.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_with_invalid_username_unsuccessful(self):
        """Test creating a new user with invalid username is unsuccessful"""
        payload = {
            "password": "@strong#password",
            "is_superuser": False,
            "is_staff": False,
            "username": "Sample User",
            "is_active": True,
            "groups": [],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_invalid_password_unsuccessful(self):
        """Test creating a new user with invalid password is unsuccessful"""
        payload = {
            "password": "123",
            "is_superuser": False,
            "is_staff": False,
            "username": "sample_user@ticketing.sample",
            "is_active": True,
            "groups": [],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_duplicate_username_unsuccessful(self):
        """Test creating a new user with duplicate username is unsuccessful"""
        instance = sample_user()
        payload = {
            "password": "@strong#password",
            "is_superuser": False,
            "is_staff": False,
            "username": instance.username,
            "is_active": True,
            "groups": [],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_superuser_successful(self):
        """Test creating a new superuser is successful"""
        payload = {
            "password": "@strong#password",
            "is_superuser": True,
            "is_staff": True,
            "username": "sample_superuser@ticketing.sample",
            "is_active": True,
            "groups": [],
            "user_permissions": []
        }
        result = self.client.post(USERS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['username'], payload['username'])
        self.assertTrue(result.data['is_superuser'])
        self.assertTrue(result.data['is_staff'])
        self.assertTrue(result.data['is_active'])
        self.assertIsNone(result.data['last_login'])

    def test_retrieve_users_successful(self):
        """Test retrieving users is successful"""
        sample_user()
        sample_user(username='user2@ticketing.sample')
        result = self.client.get(USERS_LIST_URL)
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['results'], serializer.data)

    def test_retrieve_single_user_successful(self):
        """Test retrieving a single user is successful"""
        instance = sample_user()
        result = self.client.get(reverse('api:user_management:users-detail', kwargs={'pk': instance.pk}))
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['username'], instance.username)

    def test_update_user_successful(self):
        """Test updating the user is successful"""
        instance = sample_user()
        payload = {
            'is_active': False
        }
        result = self.client.patch(
            reverse('api:user_management:users-detail', kwargs={'pk': instance.pk}),
            data=payload
        )
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['is_active'], payload['is_active'])
        self.assertNotEqual(result.data['is_active'], instance.is_active)
        self.assertFalse(result.data['is_active'])

    def test_update_user_unsuccessful(self):
        """Test updating the user is unsuccessful"""
        instance = sample_user()
        payload = {
            'username': '',
        }
        result = self.client.patch(
            reverse('api:user_management:users-detail', kwargs={'pk': instance.pk}),
            data=payload
        )
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user_successful(self):
        """Test deleting the user is successful"""
        instance = sample_user()
        result = self.client.delete(
            reverse('api:user_management:users-detail', kwargs={'pk': instance.pk}),
        )
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_user_unsuccessful(self):
        """Test deleting the user is unsuccessful"""
        result = self.client.delete(
            reverse('api:user_management:users-detail', kwargs={'pk': 10000}),
        )
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

from django.contrib.auth.models import Group, Permission
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from user_management.tests.common_functions import sample_superuser, sample_group

from user_management.serializers import GroupSerializer, PermissionSerializer

GROUPS_LIST_URL = reverse('api:user_management:groups-list')


class PublicGroupsAPITests(TestCase):
    """Test the public available groups API"""
    def setUp(self) -> None:
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving permissions"""
        result = self.client.get(GROUPS_LIST_URL)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateGroupsAPITests(TestCase):
    """Test the authorized user groups API"""
    def setUp(self) -> None:
        self.super_user = sample_superuser()
        self.client = APIClient()
        self.client.force_authenticate(self.super_user)

    def test_create_group_successful(self):
        """Test creating a new group is successful"""
        payload = {
            'name': 'Sample Group',
        }
        result = self.client.post(GROUPS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['name'], payload['name'])

    def test_create_group_with_permissions_successful(self):
        """Test creating a new group with permissions is successful"""
        permissions = Permission.objects.all()
        payload = {
            'name': 'Sample Group',
            'permission_ids': sorted([permission.pk for permission in permissions])
        }
        result = self.client.post(GROUPS_LIST_URL, payload)
        permission_serializer = PermissionSerializer(permissions, many=True)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['name'], payload['name'])
        self.assertEqual(result.data['permissions'], permission_serializer.data)

    def test_create_group_with_invalid_name_unsuccessful(self):
        """Test creating a new group with invalid name is unsuccessful"""
        payload = {
            'name': '',
        }
        result = self.client.post(GROUPS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_group_with_duplicate_name_unsuccessful(self):
        """Test creating a new group with duplicate name is unsuccessful"""
        instance = sample_group()
        payload = {
            'name': instance.name,
        }
        result = self.client.post(GROUPS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_group_with_invalid_permission_unsuccessful(self):
        """Test creating a new group with invalid permission is unsuccessful"""
        payload = {
            'name': 'Sample Group',
            'permission_ids': [123456]
        }
        result = self.client.post(GROUPS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_groups_successful(self):
        """Test retrieving groups is successful"""
        sample_group(name='Sample Group One')
        sample_group(name='Sample Group Two')
        result = self.client.get(GROUPS_LIST_URL)
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['results'], serializer.data)

    def test_retrieve_single_group(self):
        """Test retrieving a single group is successful"""
        instance = sample_group()
        result = self.client.get(reverse('api:user_management:groups-detail', kwargs={'pk': instance.pk}))
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['name'], instance.name)

    def test_update_group_successful(self):
        """Test updating the group is successful"""
        instance = sample_group()
        payload = {
            'name': 'Update Group'
        }
        result = self.client.patch(
            reverse('api:user_management:groups-detail', kwargs={'pk': instance.pk}),
            data=payload
        )
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['name'], payload['name'])
        self.assertNotEqual(result.data['name'], instance.name)

    def test_update_group_unsuccessful(self):
        """Test updating the group is unsuccessful"""
        instance = sample_group()
        payload = {
            'name': '',
        }
        result = self.client.patch(
            reverse('api:user_management:groups-detail', kwargs={'pk': instance.pk}),
            data=payload
        )
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_group_successful(self):
        """Test deleting the group is successful"""
        instance = sample_group()
        result = self.client.delete(
            reverse('api:user_management:groups-detail', kwargs={'pk': instance.pk}),
        )
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_group_unsuccessful(self):
        """Test deleting the group is unsuccessful"""
        result = self.client.delete(
            reverse('api:user_management:groups-detail', kwargs={'pk': 123}),
        )
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

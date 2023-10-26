from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from user_management.tests.common_functions import sample_superuser

from user_management.serializers import PermissionSerializer

PERMISSIONS_LIST_URL = reverse('api:user_management:permissions-list')


class PublicPermissionsAPITests(TestCase):
    """Test the public available permissions API"""
    def setUp(self) -> None:
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving permissions"""
        result = self.client.get(PERMISSIONS_LIST_URL)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePermissionsAPITests(TestCase):
    """Test the authorized user permissions API"""
    def setUp(self) -> None:
        self.super_user = sample_superuser()
        self.client = APIClient()
        self.client.force_authenticate(self.super_user)

    def test_retrieve_permissions(self):
        """Test retrieving the permissions"""
        result = self.client.get(PERMISSIONS_LIST_URL)
        permissions = Permission.objects.all().order_by('id')[:20]
        serializer = PermissionSerializer(permissions, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['results'], serializer.data)

    def test_retrieve_single_permission(self):
        """Test retrieving a single permission"""
        instance = Permission.objects.get(pk=1)
        result = self.client.get(reverse('api:user_management:permissions-detail', kwargs={'pk': instance.pk}))
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['name'], instance.name)
        self.assertEqual(result.data['codename'], instance.codename)

    def test_create_permission_not_allowed(self):
        """Test creating a new permission is not allowed"""
        payload = {
            'name': 'Sample Permission',
            'content_type_id': 1,
            'codename': 'sample_permission',
        }
        result = self.client.post(PERMISSIONS_LIST_URL, payload)
        self.assertEqual(result.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_permission_not_allowed(self):
        """Test updating the permission is not allowed"""
        instance = Permission.objects.get(pk=1)
        result = self.client.patch(
            reverse('api:user_management:permissions-detail', kwargs={'pk': instance.pk}),
            data={
                'name': 'Other Name',
            }
        )
        self.assertEqual(result.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_permission_not_allowed(self):
        """Test deleting the permission is not allowed"""
        instance = Permission.objects.get(pk=1)
        result = self.client.delete(reverse('api:user_management:permissions-detail', kwargs={'pk': instance.pk}))
        self.assertEqual(result.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

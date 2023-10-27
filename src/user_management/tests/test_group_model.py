from django.contrib.auth.models import Group, Permission
from django.db.utils import IntegrityError
from django.test import TestCase

from .common_functions import sample_group


class GroupModelTest(TestCase):
    def test_create_group_successful(self):
        """Test creating a new group is successful"""
        defaults = {
            'name': 'Sample Group'
        }
        instance = Group.objects.create(**defaults)
        self.assertEqual(instance.name, defaults['name'])

    def test_create_group_with_permissions_successful(self):
        """Test creating a new group with permissions is successful"""
        permissions = sorted(list(Permission.objects.values_list('id', flat=True)))
        defaults = {
            'name': 'Sample Group'
        }
        instance = Group.objects.create(**defaults)
        instance.permissions.set(permissions)
        self.assertEqual(instance.name, defaults['name'])
        self.assertEqual(sorted([permission.id for permission in instance.permissions.all()]), permissions)

    def test_creating_group_with_none_name(self):
        """Test creating a new group with a none name"""
        with self.assertRaises(IntegrityError):
            Group.objects.create(name=None)

    def test_create_new_group_with_duplicate_name_unsuccessful(self):
        """Test creating a new group with duplicate name is unsuccessful"""
        group = sample_group()
        with self.assertRaises(IntegrityError):
            Group.objects.create(name=group.name)

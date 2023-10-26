from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


def sample_user(**params):
    """
    Create and return a sample user object
    """
    defaults = {
        'username': 'user@ticketing.sample',
        'password': '1234@Pass'
    }
    defaults.update(params)
    return get_user_model().objects.create_user(**defaults)


def sample_superuser(**params):
    """
    Create and return a sample superuser object
    """
    defaults = {
        'username': 'superuser@ticketing.sample',
        'password': '1234@Pass'
    }
    defaults.update(params)
    return get_user_model().objects.create_superuser(**defaults)


def sample_group(**params):
    """
    Create and return a sample group object
    """
    defaults = {
        'name': 'Sample Group',
    }
    defaults.update(params)
    return Group.objects.create(**defaults)

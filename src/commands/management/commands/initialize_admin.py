from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import os


class Command(BaseCommand):
    """ Create default superuser """

    def handle(self, *args, **kwargs):
        admin_username = os.environ.get("ADMIN_USERNAME", "admin@ticketing.sample")

        if not get_user_model().objects.filter(username=admin_username).exists():
            get_user_model().objects.create_superuser(
                password=os.environ.get("ADMIN_PASSWORD", "admin@control*987"),
                username=admin_username
            )
        else:
            print(f'An admin user with username = {admin_username} exists')

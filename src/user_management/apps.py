from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_management'
    verbose_name = _('User Management')

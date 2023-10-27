from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class CommandsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commands'
    verbose_name = _('Commands')

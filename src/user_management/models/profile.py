from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt
from extensions.choices import GenderChoices


class Profile(AbstractCreatAtUpdateAt, models.Model):
    user = models.OneToOneField(
        get_user_model(),
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_profile_user'
    )
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=200
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=200
    )
    gender = models.PositiveSmallIntegerField(
        verbose_name=_('Gender'),
        choices=GenderChoices.choices
    )

    class Meta:
        app_label = 'user_management'
        db_table = 'user_management_profiles'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ['user_id']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

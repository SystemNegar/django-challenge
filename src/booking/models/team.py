from django.utils.translation import gettext_lazy as _
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt


class Team(AbstractCreatAtUpdateAt, models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=200,
        unique=True,
        db_index=True
    )

    class Meta:
        app_label = 'booking'
        db_table = 'booking_teams'
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
        ordering = ['id']

    def __str__(self) -> str:
        return self.name.__str__()

from django.utils.translation import gettext_lazy as _
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt


class Stadium(AbstractCreatAtUpdateAt, models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=200,
        db_index=True
    )
    province = models.CharField(
        verbose_name=_('Province'),
        max_length=200,
        db_index=True
    )
    city = models.CharField(
        verbose_name=_('City'),
        max_length=200,
        db_index=True
    )
    address = models.TextField(
        verbose_name=_('Address'),
        blank=True
    )
    map_url = models.URLField(
        verbose_name=_('Map URL'),
        blank=True
    )

    class Meta:
        app_label = 'booking'
        db_table = 'booking_stadiums'
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')
        ordering = ['id']
        unique_together = ['name', 'province', 'city']

    def __str__(self) -> str:
        return f"{self.province} - {self.city} - {self.name}"

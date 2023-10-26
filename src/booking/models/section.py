from django.utils.translation import gettext_lazy as _
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt
from extensions.choices import LocationChoices


class Section(AbstractCreatAtUpdateAt, models.Model):
    stadium = models.ForeignKey(
        'Stadium',
        verbose_name=_('Stadium'),
        on_delete=models.CASCADE,
        related_name='section_stadiums'
    )
    location = models.PositiveSmallIntegerField(
        verbose_name=_('Location'),
        choices=LocationChoices.choices,
    )
    capacity = models.PositiveSmallIntegerField(
        verbose_name=_('Capacity')
    )

    class Meta:
        app_label = 'booking'
        db_table = 'booking_sections'
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ['id']
        unique_together = ['stadium', 'location']

    def __str__(self) -> str:
        return f"{self.stadium} - {self.location}"

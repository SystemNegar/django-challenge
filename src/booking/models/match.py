from django.utils.translation import gettext_lazy as _
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt


class Match(AbstractCreatAtUpdateAt, models.Model):
    stadium = models.ForeignKey(
        'Stadium',
        verbose_name=_('Stadium'),
        on_delete=models.PROTECT,
        related_name='match_stadiums'
    )
    host_team = models.ForeignKey(
        'Team',
        verbose_name=_('Host Team'),
        on_delete=models.PROTECT,
        related_name='match_host_teams'
    )
    guest_team = models.ForeignKey(
        'Team',
        verbose_name=_('Guest Team'),
        on_delete=models.PROTECT,
        related_name='match_guest_teams'
    )
    start_time = models.DateTimeField(
        verbose_name=_('Start Time')
    )

    class Meta:
        app_label = 'booking'
        db_table = 'booking_matches'
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')
        ordering = ['id']
        unique_together = ['stadium', 'host_team', 'guest_team', 'start_time']

    def __str__(self) -> str:
        return f"{self.stadium} - {self.host_team} & {self.guest_team} - {self.start_time}"

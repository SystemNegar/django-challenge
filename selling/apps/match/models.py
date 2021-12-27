from django.db import models
from django.utils import timezone

from selling.apps.stadium.models import Stadium


class Match(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True
    )
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    team1 = models.CharField(
        max_length=255,
        db_index=True,
        null=True
    )
    team2 = models.CharField(
        max_length=255,
        db_index=True,
        null=True
    )
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
    )

    class Meta:
        unique_together = ['name', 'stadium', 'date', 'time']

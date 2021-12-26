from django.db import models
from django.utils import timezone


class Stadium(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        unique=True
    )
    capacity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
    )

    def __str__(self):
        return self.name

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils import timezone

from selling.apps.match.models import Match


class Seat(models.Model):
    name = models.CharField(max_length=255)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through='BookSeat')
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
    )

    class Meta:
        unique_together = ['name', 'match']

    def __str__(self):
        return self.name


class BookSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        default=timezone.now,
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_index=True,
    )
    reserved = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['seat'],
                condition=Q(reserved=True),
                name='unique seat'
            ),
        ]

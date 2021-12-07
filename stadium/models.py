from django.db import models
from django.utils import timezone


class Stadium(models.Model):
    name = models.CharField(max_length=150)
    founded_in = models.DateTimeField(editable=False)
    capacity = models.IntegerField()

    def save(self, *args, **kwargs):
        self.founded_in = timezone.now()
        return super(Stadium, self).save(*args, **kwargs)

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from arman.city.models import City


class Stadium(TimeStampedModel):
    name = models.CharField(max_length=256, blank=False, null=False)
    address = models.CharField(max_length=1024, blank=False, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="stadiums")

    class Meta:
        db_table = "stadiums"
        verbose_name = _("stadium")
        verbose_name_plural = _("Stadium")

    def __str__(self):
        return self.name

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class City(TimeStampedModel):
    name = models.CharField(max_length=256, blank=False, null=False)

    class Meta:
        db_table = "cities"
        verbose_name = _("city")
        verbose_name_plural = _("City")


class Stadium(TimeStampedModel):
    name = models.CharField(max_length=256, blank=False, null=False)
    address = models.CharField(max_length=1024, blank=False, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="stadiums")

    class Meta:
        db_table = "stadiums"
        verbose_name = _("stadium")
        verbose_name_plural = _("Stadium")

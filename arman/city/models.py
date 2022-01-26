from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class City(TimeStampedModel):
    name = models.CharField(max_length=256, blank=False, null=False)

    class Meta:
        db_table = "cities"
        verbose_name = _("city")
        verbose_name_plural = _("City")

    def __str__(self):
        return self.name

from django.utils.translation import gettext_lazy as _
from django.db import models


class AbstractCreatAtUpdateAt(models.Model):
    create_at = models.DateTimeField(
        verbose_name=_('Create At'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated At'),
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True

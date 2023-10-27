from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt
from extensions.choices import InvoiceStatusChoices

from decimal import Decimal


class Invoice(AbstractCreatAtUpdateAt, models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='invoice_users'
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_('Status'),
        choices=InvoiceStatusChoices.choices,
        default=InvoiceStatusChoices.UNPAID
    )

    class Meta:
        app_label = 'booking'
        db_table = 'booking_invoices'
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')
        ordering = ['id']

    def __str__(self) -> str:
        return f"{self.user} - {self.id}"

    @property
    def get_total_amount(self) -> Decimal:
        return sum([item['section__price'] for item in self.ticket_invoices.values('section__price')])

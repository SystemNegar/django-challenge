from django.utils.translation import gettext_lazy as _
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt
from extensions.choices import PaymentStatusChoices


class Payment(models.Model):
    invoice = models.ForeignKey(
        'Invoice',
        verbose_name=_('Invoice'),
        on_delete=models.CASCADE,
        related_name='payment_invoices'
    )
    amount = models.DecimalField(
        verbose_name=_('Amount'),
        decimal_places=2,
        max_digits=14
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_('Status'),
        choices=PaymentStatusChoices.choices
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created At'),
        auto_now_add=True,
        editable=False
    )

    class Meta:
        app_label = 'booking'
        db_table = 'booking_payments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        ordering = ['id']

    def __str__(self) -> str:
        return f"Payment - {self.id}"

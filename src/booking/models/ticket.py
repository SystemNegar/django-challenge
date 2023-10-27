from django.utils.translation import gettext_lazy as _
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt
from extensions.choices import TicketStatusChoices


class Ticket(AbstractCreatAtUpdateAt, models.Model):
    invoice = models.ForeignKey(
        'Invoice',
        verbose_name=_('Invoice'),
        on_delete=models.PROTECT,
        related_name='ticket_invoices'
    )
    match = models.ForeignKey(
        'Match',
        verbose_name=_('Match'),
        on_delete=models.PROTECT,
        related_name='ticket_matches'
    )
    section = models.ForeignKey(
        'Section',
        verbose_name=_('Section'),
        on_delete=models.PROTECT,
        related_name='ticket_sections'
    )
    seat_number = models.PositiveSmallIntegerField(
        verbose_name=_('Seat Number')
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_('Status'),
        choices=TicketStatusChoices.choices,
        default=TicketStatusChoices.RESERVED
    )

    class Meta:
        app_label = 'booking'
        db_table = 'booking_tickets'
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ['id']

    def __str__(self) -> str:
        return f"Ticket {self.id}"

    def set_as_sold(self) -> None:
        """It will change the status field and save the object"""
        self.status = TicketStatusChoices.SOLD
        self.save()

from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class GenderChoices(IntegerChoices):
    """Enum class for the gender fields"""
    MALE = 0, _('Male')
    FEMALE = 1, _('Female')

    __empty__ = '---------'


class LocationChoices(IntegerChoices):
    """Enum class for the location fields"""
    A = 0, _('A')
    B = 1, _('B')
    C = 2, _('C')
    VIP = 3, _('VIP')


class InvoiceStatusChoices(IntegerChoices):
    """Enum class for the invoice status fields"""
    PAID = 0, _('Paid')
    UNPAID = 1, _('Unpaid')


class TicketStatusChoices(IntegerChoices):
    """Enum class for the ticket status fields"""
    SOLD = 0, _('Sold')
    RESERVED = 1, _('Reserved')


class PaymentStatusChoices(IntegerChoices):
    """Enum class for the payment status fields"""
    SUCCESSFUL = 0, _('Successful')
    UNSUCCESSFUL = 1, _('Unsuccessful')

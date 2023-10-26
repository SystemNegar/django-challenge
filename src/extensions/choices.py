from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class GenderChoices(IntegerChoices):
    """Enum class for the gender fields"""
    MALE = 0, _('Male')
    FEMALE = 1, _('Female')

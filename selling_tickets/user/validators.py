from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UnicodeMobileNumberValidator(validators.RegexValidator):
    """
    validate mmobile_number
    """
    regex = r'09(\d{9})$'
    message = 'Enter a valid mobile number'
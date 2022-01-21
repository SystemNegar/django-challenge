import jwt
from django.conf import settings as django_settings
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils.crypto import get_random_string

from .models import OTP


def _create_otp():
    """
    Returns a unique random `OTP` for given `TOKEN_LENGTH` in the settings.
    """
    token_length = django_settings.OTP.get("TOKEN_LENGTH")
    return get_random_string(token_length, allowed_chars="0123456789")


def _generate_token(phone, state):
    """
    Returns a unique session_token for
    identifying a particular device in subsequent calls.
    """
    data = {"phone_number": phone, "state": state}
    session_token = jwt.encode(data, django_settings.SECRET_KEY)
    try:
        return session_token.decode()
    except AttributeError:
        return session_token


def _send_sms(otp):
    """
    Send sms to user
    :param otp:
    :return:
    """
    pass


def user_signup(phone):
    """
    user signup
    :param phone:
    :return:
    """
    try:
        otp = _create_otp()
        obj, created = OTP.objects.update_or_create(phone=phone, otp=otp)
    except IntegrityError:
        raise ValidationError({"phone": "Phone already exists"})
    _send_sms(otp)
    return _generate_token(phone=phone, state="verify")

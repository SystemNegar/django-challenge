from django.conf import settings as django_settings
from django.utils import timezone
from django.utils.crypto import get_random_string
from rest_framework_simplejwt.tokens import RefreshToken

from .models import OTP, CustomUser
from .selectors import get_otp_with_phone, get_user_with_phone


def _generate_otp():
    """
    Returns a unique random `OTP` for given `TOKEN_LENGTH` in the settings.
    """
    token_length = django_settings.OTP.get("TOKEN_LENGTH")
    return get_random_string(token_length, allowed_chars="0123456789")


def _generate_token(user):
    """
    Returns a unique token for authenticated user
    """
    return RefreshToken.for_user(user)


def _send_sms(otp):
    """
    Send sms to user
    :param otp:
    :return:
    """
    pass


def register(phone):
    """
    Register phone number and send otp code
    :param phone:
    :return:
    """
    otp = _generate_otp()
    otp_object = get_otp_with_phone(phone)
    if otp_object.exists():
        OTP.objects.filter(phone=phone).delete()
    OTP.objects.create(phone=phone, otp=otp)

    _send_sms(otp)


def _check_otp_expiry(stored_otp):
    """
    Returns True if the `otp`  not expired.
    """
    time_difference = timezone.now() - stored_otp.created
    if time_difference.seconds < django_settings.OTP.get("EXPIRATION_TIME"):
        return True
    return False


def login(otp, phone):
    if otp and phone:
        otp_stored = get_otp_with_phone(phone)
        if otp_stored.exists():
            otp_stored = otp_stored.first()
            old_otp = otp_stored.otp
            if str(old_otp) == str(otp) and _check_otp_expiry(otp_stored):
                otp_stored.register_flag = True
                otp_stored.save()
                user = get_user_with_phone(phone)
                if user.exists():
                    user = user.first()
                else:
                    user = CustomUser(phone=phone)
                    user.save()

                refresh = _generate_token(user)
                return {"access": str(refresh.access_token), "refresh": str(refresh)}
            else:
                raise ValueError("Incorrect OTP")
        else:
            raise ValueError("Phone not registered")
    else:
        raise ValueError("Phone or OTP was not received")

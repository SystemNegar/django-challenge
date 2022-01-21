from .models import OTP


def get_otp_with_phone(phone):
    return OTP.objects.filter(phone__iexact=phone)

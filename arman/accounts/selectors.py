from .models import OTP, CustomUser


def get_otp_with_phone(phone):
    return OTP.objects.filter(phone__iexact=phone)


def get_user_with_phone(phone):
    return CustomUser.objects.filter(phone__iexact=phone)

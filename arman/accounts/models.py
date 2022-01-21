from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, UUIDModel
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser, UUIDModel):
    phone = PhoneNumberField(_("Phone"), unique=True, null=True, blank=True)


class OTP(TimeStampedModel):
    phone = PhoneNumberField(_("Phone"), unique=True, null=True, blank=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    register_flag = models.BooleanField(default=False)
    expired_date = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(minutes=1)
    )

    def __str__(self):
        return str(self.otp) + " sent to " + str(self.phone)

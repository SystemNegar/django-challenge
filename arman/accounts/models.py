from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone = PhoneNumberField(_("Phone"), unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.phone)


class OTP(TimeStampedModel):
    phone = PhoneNumberField(_("Phone"), unique=True, null=True, blank=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    register_flag = models.BooleanField(default=False)

    def __str__(self):
        return str(self.otp) + " sent to " + str(self.phone)

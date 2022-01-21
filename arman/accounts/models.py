from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from model_utils.models import UUIDModel


class CustomUser(AbstractUser, UUIDModel):
    phone_regex = RegexValidator(
        regex=r"^(0|\+98)?([ ]|-|[()]){0,2}9[0|1|2|3|4|9]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}$",
        message="invalid phone number",
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)

from django.db import models
from user.base_user import MyUserManager
from django.contrib.auth.models import AbstractUser
from user.validators import UnicodeMobileNumberValidator
    

class CustomUser(AbstractUser):
    """
    customize user model to authenticate user by mobile_number
    both user and superUser username_field is mobile_number
    """
    username = None
    mobile_number = models.CharField(max_length=50,
        unique=True,
        verbose_name='Mobile Number',
        validators=[UnicodeMobileNumberValidator],
        error_messages={
         'unique': "A user with that mobile number already exists.",
         },
     )
    national_code = models.CharField(max_length=10, verbose_name='National Code', blank=True)
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []
    objects = MyUserManager()



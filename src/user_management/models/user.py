from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

from extensions.abstract_models import AbstractCreatAtUpdateAt
from user_management.managers import UserManager


class User(AbstractBaseUser, AbstractCreatAtUpdateAt, PermissionsMixin):
    """
    Custom user model to authenticate user by email address,
    Verification of users by sending an activation link to their email is not implemented.
    """
    username = models.EmailField(
        verbose_name=_('Username'),
        unique=True,
        db_index=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('Is Staff'),
        default=False
    )
    # This should change to true after sending the activation email, but is ignored here.
    is_active = models.BooleanField(
        verbose_name=_('Is Active'),
        default=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'user_management'
        db_table = 'user_management_users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username.__str__()

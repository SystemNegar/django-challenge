from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    """
    Custom user model manager where mobile_number is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True
    def __create_user(self, mobile_number, password, **extra_fields):
        if not mobile_number:
            raise ValueError('The mobile_number must be set')
        mobile_number = self.normalize_mobile_number(mobile_number)
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.__create_user(mobile_number, password, **extra_fields)

    def create_superuser(self, mobile_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.__create_user(mobile_number, password, **extra_fields)

    def normalize_mobile_number(self, mobile_number):
        return mobile_number
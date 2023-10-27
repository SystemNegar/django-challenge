from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Manager class for the 'user' model"""
    use_in_migrations = True

    def create_user(self, password, **extra_fields):
        """This will create a new regular user"""
        user = self.model(**extra_fields)
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, password, **extra_fields):
        """This will create a new staff user"""
        user = self.model(**extra_fields)
        user.is_staff = True
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **extra_fields):
        """This will create a new super admin user"""
        user = self.model(**extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

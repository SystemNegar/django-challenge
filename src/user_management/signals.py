from django.db.models.signals import post_save
from django.dispatch import receiver

from user_management.models import User, Profile


@receiver(post_save, sender=User)
def creating_profile(sender, instance, created, raw, using, **kwargs):
    """It will create a new profile instance for the user"""
    if created:
        Profile.objects.create(user=instance)

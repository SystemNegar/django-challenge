from django.db import models
from adminstrationapp.models import *
from django.contrib.auth.models import User

# Create your models here.
class UserSeat(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    seat_no = models.CharField(max_length=100)
    team_name = models.CharField(max_length=255)


    def __str__(self):
        return '{0} -> {1}'.format(self.user, self.match)

    class Meta:
        unique_together = ['match', 'user']


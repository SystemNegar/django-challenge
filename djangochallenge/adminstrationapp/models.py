from django.db import models

# Create your models here.

class Stadium(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Match(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    teams = models.CharField(max_length=255)
    match_date = models.DateTimeField()
    match_length = models.CharField(max_length=4, verbose_name='Match Length in minutes')
    
    def __str__(self):
        return self.teams


class SeatManager(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    seat_range = models.CharField(max_length=100)
    last_seat_number = models.CharField(max_length=10, default=0)

    def __str__(self):
        return '{0} -> {1}'.format(self.match, self.team_name)

    class Meta:
        unique_together = ['match', 'team_name']


from django.db import models
from stadium.models import Stadium


class Match(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} VS. {self.team2}"

    @classmethod
    def is_reserved(self, reserved_dt):
        reserved_matches = Match.objects.all()
        for match in reserved_matches:
            if match.event_date == reserved_dt:
                return False
        return True

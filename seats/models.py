from django.db import models
from matches.models import Match
from django.contrib.auth.models import User


class Seat(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    reserved = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    column = models.IntegerField()
    row = models.IntegerField()
    seat_num = models.IntegerField()

    def __str__(self):
        return f"Seat number {self.seat_num} are located in row {self.row} and column {self.column}"

    @classmethod
    def check_available(cls, seat_num):
        pass

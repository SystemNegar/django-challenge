from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=50, verbose_name='Stadium Name')
    city = models.CharField(max_length=50, blank=True, verbose_name='Stadium City')
    address = models.TextField(verbose_name='Stadium Address')

    def __str__(self) -> str:
        return self.name

class StadiumPlace(models.Model):
    stadium = models.ForeignKey('Stadium', on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=50, verbose_name='Place Name', unique=True)
    number_of_rows = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return ("stadium: %s place: %s") % (self.stadium, self.name)


class PlaceSeats(models.Model):
    place = models.ForeignKey('StadiumPlace', on_delete=models.CASCADE, related_name='place_seats')
    row_number = models.IntegerField()
    number_of_seats_per_row = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return ("%s row_number: %s") % (self.place, self.row_number) 

    class Meta:
        unique_together = ['place', 'row_number']

class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Team Name', unique=True)

    def __str__(self) -> str:
        return self.name


class Match(models.Model):
    stadium = models.ForeignKey('Stadium', on_delete=models.CASCADE, related_name='matches')
    host_team = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='host_team')
    guest_team = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='guest_team')
    start_time = models.DateTimeField()

    def __str__(self) -> str:
        return "%s VS %s, Date: %s" % (self.host_team, self.guest_team, self.start_time)

    class Meta:
        unique_together = ['stadium', 'start_time']



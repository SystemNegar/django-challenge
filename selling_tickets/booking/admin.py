from django.contrib import admin
from booking.models import Stadium, StadiumPlace, PlaceSeats, Match, Team
# Register your models here.
admin.site.register(Stadium)
admin.site.register(StadiumPlace)
admin.site.register(PlaceSeats)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Ticket)
admin.site.register(Invoice)
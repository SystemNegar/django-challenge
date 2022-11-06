from django.contrib import admin
from booking.models import Stadium, StadiumPlace, PlaceSeats
# Register your models here.

admin.site.register(Stadium)
admin.site.register(StadiumPlace)
admin.site.register(PlaceSeats)

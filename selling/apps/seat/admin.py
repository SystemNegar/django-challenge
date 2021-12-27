from django.contrib import admin

from selling.apps.seat.models import Seat, BookSeat

admin.site.register(Seat)
admin.site.register(BookSeat)

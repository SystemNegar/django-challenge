from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "capacity")

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("id", "stadium", "teams", "match_date")


@admin.register(SeatManager)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("id", "team_name", "match", "seat_range")

from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(UserSeat)
class UserSeatAdmin(admin.ModelAdmin):
    list_display = ("id", "team_name", "user", "match")


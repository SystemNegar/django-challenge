from django.contrib import admin

from selling.apps.match.models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'stadium',
        'team1',
        'team2',
        'date',
        'time'
    )
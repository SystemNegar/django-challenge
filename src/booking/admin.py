from django.contrib import admin

from booking.models import Stadium, Section, Team


class SectionInlineAdmin(admin.TabularInline):
    model = Section
    min_num = 1
    extra = 0


class StadiumAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'province',
        'city',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'province',
        'city',
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'name',
        'province',
        'city',
    ]

    actions = [
        'delete_selected',
    ]

    inlines = (
        SectionInlineAdmin,
    )

    def get_queryset(self, request):
        return self.model.objects.prefetch_related('section_stadiums')


class TeamAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'name',
    ]

    actions = [
        'delete_selected',
    ]


admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Team, TeamAdmin)

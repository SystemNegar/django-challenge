from django.contrib import admin

from booking.models import Stadium, Section, Team, Match, Invoice, Ticket, Payment


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


class MatchAdmin(admin.ModelAdmin):
    list_display = [
        'stadium',
        'host_team',
        'guest_team',
        'start_time',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'stadium',
        'host_team',
        'guest_team',
        'start_time',
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'stadium',
        'host_team',
        'guest_team',
    ]

    actions = [
        'delete_selected',
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related('stadium', 'host_team', 'guest_team')


class InvoiceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = [
        'user',
        'status',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'status',
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'user',
    ]

    actions = [
        'delete_selected',
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related('user')


class TicketAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = [
        'match',
        'section',
        'seat_number',
        'status',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'match',
        'section',
        'status',
        'created_at',
        'updated_at',
    ]

    search_fields = [
        'match',
        'section',
        'seat_number',
    ]

    actions = [
        'delete_selected',
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related('invoice', 'match', 'section')


class PaymentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = [
        'invoice',
        'amount',
        'status',
        'created_at',
    ]

    list_filter = [
        'status',
        'created_at',
    ]

    search_fields = [
        'invoice',
        'amount',
    ]

    actions = [
        'delete_selected',
    ]

    def get_queryset(self, request):
        return self.model.objects.select_related('invoice')


admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Payment, PaymentAdmin)

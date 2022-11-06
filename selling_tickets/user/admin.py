
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.forms import CustomUserCreationForm, CustomUserChangeForm
from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('mobile_number', 'is_staff', 'is_active', 'national_code')
    list_filter = ('mobile_number', 'is_staff', 'is_active', 'national_code')
    fieldsets = (
        (None, {'fields': ('mobile_number', 'password', 'national_code')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number', 'password1', 'password2', 'national_code', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('mobile_number', 'national_code')
    ordering = ('mobile_number',)


admin.site.register(CustomUser, CustomUserAdmin)

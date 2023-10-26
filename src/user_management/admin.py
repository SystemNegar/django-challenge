from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from user_management.models import User, Profile


class ProfileInlineAdmin(admin.TabularInline):
    model = Profile


class UserAdmin(BaseUserAdmin):
    list_display = [
        'username',
        'get_full_name',
        'is_active',
        'is_superuser',
        'is_staff',
        'created_at',
        'updated_at',
        'last_login'
    ]

    list_filter = [
        'is_active',
        'is_superuser',
        'is_staff',
        'created_at',
        'updated_at',
        'last_login',
    ]

    search_fields = [
        'username',
    ]

    actions = [
        'delete_selected',
    ]

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_("Access Control"), {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups')}),
        (_("Important Date"), {'fields': ('created_at', 'updated_at', 'last_login')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
        (_("Access Control"), {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups')}),
    )

    readonly_fields = [
        'created_at',
        'updated_at',
        'last_login',
    ]

    inlines = (
        ProfileInlineAdmin,
    )

    def get_queryset(self, request):
        return self.model.objects.select_related('user_profile_user')

    def get_full_name(self, obj):
        return obj.user_profile_user.get_full_name

    get_full_name.short_description = _('Full Name')


admin.site.register(User, UserAdmin)

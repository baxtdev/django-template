from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User,ResetPasword


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'email', 
        'get_full_name', 
        'phone', 
        'last_activity'
        )
    fieldsets = (
        (None, {'fields': (
            'email',
            'phone',
            'password',
        )}),
        (_('Personal info'), {'fields': (
            'image',
            'first_name',
            'last_name',
            'middle_name'
        )}),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (_('Important dates'), {'fields': (
            'date_joined',
            'last_login',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'phone',
                'password1',
                'password2',
            ),
        }),
    )

    search_fields = (
        'email', 
        'first_name', 
        'last_name'
        )
    
    ordering = ('email',)


@admin.register(ResetPasword)
class ResetPasswordAdmin(admin.ModelAdmin):
    pass
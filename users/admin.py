from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm, UserUpdateForm
from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ['email', 'first_name',
                    'last_name', 'phone_number', 'manager']

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)

    def phone_number(self, obj):
        return obj.profile.phone_number
    phone_number.short_description = 'Phone number'

    def manager(self, obj):
        return f'{obj.profile.manager.first_name} {obj.profile.manager.last_name}' if obj.profile.manager else 'N/A'
    manager.short_description = 'Manager'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'allow_notifications', 'manager')
    readonly_fields = ('manager', )

    # Set current user as the manager
    def save_model(self, request, obj, form, change):
        if not obj.manager:
            obj.manager = request.user
        super().save_model(request, obj, form, change)

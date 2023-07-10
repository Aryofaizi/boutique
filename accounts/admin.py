from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = UserAdmin.list_display + ("phone_number", )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone_number",)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone_number",)}),
    )



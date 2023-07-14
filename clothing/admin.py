from django.contrib import admin
from .models import Clothes


@admin.register(Clothes)
class ClothAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "cloth_type")

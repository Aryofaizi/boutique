from django.contrib import admin
from .models import Clothes, ClothType


@admin.register(Clothes)
class ClothAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "cloth_type")


@admin.register(ClothType)
class ClothTypeAdmin(admin.ModelAdmin):
    list_display = ("choices", "color",)

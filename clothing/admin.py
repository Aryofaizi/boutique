from django.contrib import admin
from .models import Cloth, ClothType, ClothColor


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)


@admin.register(ClothType)
class ClothTypeAdmin(admin.ModelAdmin):
    list_display = ("cloth_choices", )


@admin.register(ClothColor)
class ClothColorAdmin(admin.ModelAdmin):
    list_display = ("cloth_color", )

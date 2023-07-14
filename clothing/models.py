from django.db import models
from accounts.models import CustomUser


class ClothColor(models.Model):
    cloth_color = models.CharField(max_length=50, default="black")

    def __str__(self):
        return self.cloth_color


class ClothType(models.Model):
    cloth_choices = models.CharField(max_length=50, default="t-shirt")

    def __str__(self):
        return self.cloth_choices


class Cloth(models.Model):
    name = models.CharField(max_length=100)
    cloth_width = models.IntegerField(null=True, blank=True)
    cloth_length = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    designers = models.CharField(max_length=100)
    description = models.TextField()
    choices = models.ForeignKey(ClothType, on_delete=models.CASCADE, related_name="type")
    color = models.ForeignKey(ClothColor, on_delete=models.CASCADE, related_name="color")

    def __str__(self):
        return self.name



from django.db import models
from accounts.models import CustomUser


class ClothType(models.Model):
    choices = models.CharField(max_length=100)
    color = models.CharField(max_length=50)


class Clothes(models.Model):
    name = models.CharField(max_length=100)
    cloth_type = models.ForeignKey(ClothType, on_delete=models.CASCADE)
    cloth_width = models.IntegerField(null=True, blank=True)
    cloth_length = models.IntegerField(null=True, blank=True)
    cloth_color = models.ForeignKey(ClothType, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    designers = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.cloth_type}"

from django.db import models
from .category import Categories


class Product(models.Model):
    barcode = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=150, unique=True)
    brands = models.CharField(max_length=150)
    url = models.URLField()
    url_image = models.URLField()
    url_image_small = models.URLField()
    nutrition_score = models.CharField(max_length=1)
    energy_100g = models.FloatField(default=0, null=True)
    sugars_100g = models.FloatField(default=0, null=True)
    sodium_100g = models.FloatField(default=0, null=True)
    fat_100g = models.FloatField(default=0, null=True)
    salt_100g = models.FloatField(default=0, null=True)
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return f"{self.name}, {self.nutrition_score}"

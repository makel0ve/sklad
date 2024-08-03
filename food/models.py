from django.db import models
from django.contrib import admin
from product.models import Productone

class Food(models.Model):
    name = models.CharField(max_length = 40)
    time_relise = models.IntegerField(null=True)
    countfood = models.FloatField(null = True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    ingredient_name = models.ForeignKey(Productone, on_delete=models.CASCADE, null=True)
    need = models.FloatField(null=True)

    def __str__(self):
        return str(self.name)
from django.db import models

class Productone(models.Model):
    name = models.CharField(max_length = 40)
    weigth_product = models.FloatField()
    pricekg = models.FloatField()

    def __str__(self):
        return self.name
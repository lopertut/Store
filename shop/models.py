from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100)


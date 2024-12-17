from django.contrib.auth.models import User
from django.db import models
from catalog.models import Products


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_quantity = models.PositiveIntegerField()
    order_date = models.DateField()


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

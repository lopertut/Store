from django.db import models
from django.contrib.auth.models import User
from catalog.models import Products


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}, {self.product.name}, {self.quantity}"

    class Meta:
        unique_together = (('user', 'product'),)

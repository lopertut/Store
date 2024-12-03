from django.db import models
from django.contrib.auth.models import User
from catalog.models import Products
from django.utils.timezone import now


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Cart of {self.user.username} created on {self.created_date}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart {self.cart.id}"

    class Meta:
        unique_together = (('cart', 'product'),)


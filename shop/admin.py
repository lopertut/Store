from django.contrib import admin
from .models import *


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')
    list_filter = ('user', 'product')
    search_fields = ('user__username', 'product__name')

from django.contrib import admin
from models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('name',)

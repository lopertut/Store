from django.shortcuts import render
from .models import Products


def index(request):
    return render(request, '../templates/index.html')


def catalog(request):
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'catalog.html', context)

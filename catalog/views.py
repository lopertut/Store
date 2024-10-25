from django.shortcuts import render
from .models import Products


def catalog(request):
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'catalog.html', context)

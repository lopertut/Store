from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from . authorization import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import Products, Cart


def index(request):
    return render(request, 'index.html')


@require_POST
def add_to_cart_ajax(request):
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        product = Products.objects.get(id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

        if not created:
            cart_item.quantity += quantity
        cart_item.save()
        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def shopping_cart(request,):
    return render(request, 'shopping_cart.html')


def catalog(request):
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'catalog.html', context)


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('index')

    context = {
        'login_form': form
    }

    return render(request, 'login_form.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'registration_form': form
    }

    return render(request, 'registration_form.html', context=context)

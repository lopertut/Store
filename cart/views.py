from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from .models import Products, Cart


@require_POST
@login_required
def add_to_cart_ajax(request):
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product = Products.objects.get(pk=product_id)
        quantity = data.get('quantity', 1)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@require_POST
@login_required
def remove_from_cart_ajax(request):
    try:
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity_to_remove = data.get('quantity', 1)
        cart_item = Cart.objects.get(user=request.user, product_id=product_id)

        if cart_item.quantity > quantity_to_remove:
            cart_item.quantity -= quantity_to_remove
            cart_item.save()
        else:
            cart_item.delete()
        return JsonResponse({'success': True})

    except Cart.DoesNotExist:
        return JsonResponse({'success': False})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def shopping_cart(request,):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'shopping_cart.html', context)
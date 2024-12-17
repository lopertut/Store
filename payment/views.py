from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_page(request):
    return render(request, 'checkout.html')


def create_checkout_session(request):
    try:
        checkout_session = stripe.create.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price_data': {
                'currency': 'eur',
                'product_data': {'name': 't-shirt', },
                'unit_amount': 1,
            },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/') + '?success=true',
            cancel_url=request.build_absolute_uri('/') + '?success=true',
        )
        return JsonResponse({'session_id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)})

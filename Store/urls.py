"""
URL configuration for Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from users import views as user_views
from cart import views as cart_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', user_views.login, name='login'),
    path('registration', user_views.register, name='registration'),
    path('logout', user_views.logout, name='logout'),
    path('shopping_cart', cart_views.shopping_cart, name='shopping_cart'),
    path('catalog', views.catalog, name='catalog'),
    path('add_to_cart_ajax', cart_views.add_to_cart_ajax, name='add_to_cart_ajax'),
    path('remove_from_cart_ajax', cart_views.remove_from_cart_ajax, name='remove_from_cart_ajax'),
]

"""shopengine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', main_page, name='main_page_url'),
	path('delivery/', delivery_page, name='delivery_url'),
    path('add_to_cart/', add_to_cart_view, name='add_to_cart_url'),
	path('remove_from_cart/', remove_from_cart_view, name='remove_from_cart_view_url'),
    path('checkout/', checkout, name='checkout_url'),
    path('buy/', buy, name='buy_url'),
    path('buy_one_click/', buy_one_click, name='buy_one_click_url'),
	path('buy_one_click_one/', buy_one_click_one, name='buy_one_click_one_url'),
    path('shop/<slug:menu_slug>/', cat_brand, name="cat_brand_url"),
    path('product/<slug:sub_category>/<slug:product>/', show_product_card, name="show_product_card_urls"), # карточка товара "product/samsung-s7/produkt-12/"
    path('category/<slug:category>/<slug:brand>/', shop_page, name="shop_page_url"), # страница магазина "category/chehlyi-dlya-telefonov/samsung"
    path('catalog/<slug:category>/<slug:brand>/<slug:product>/', shop_page_model, name="shop_page_model_url"), # Отфильтрованая страница "catalog/chehlyi-dlya-telefonov/samsung/samsung-s7/"
]


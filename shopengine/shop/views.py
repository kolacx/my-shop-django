from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from .models import Product, Category, ModelPhone, Menu, CartItem, Card, Order, MainPage, PropertyOrder
from .forms import OrderForm
from decimal import *

# Create your views here.

def main_page(request):
	try:
		cart_id = request.session['cart_id']
		cart = Card.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Card()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Card.objects.get(id=cart_id)
	
	get_menu = Menu.objects.all()

	get_brands = Category.objects.all()

	products_sale = Product.objects.filter(in_sale=True)
	products_new = Product.objects.filter(is_new=True)

	content_main_page = MainPage.objects.all()

	context = {
		'get_menu' : get_menu,
		'cart' : cart,
		'products_sale': products_sale,
		'products_new': products_new,
		'get_brands': get_brands,
		'content_main_page': content_main_page
	}
	return render(request, 'shop/main_page.html', context)

def cat_brand(request, menu_slug):

	try:
		cart_id = request.session['cart_id']
		cart = Card.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Card()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Card.objects.get(id=cart_id)

	menu_s = Menu.objects.filter(slug=menu_slug)

	get_menu = Menu.objects.all()

	context = {
		'menu_s': menu_s,
		'get_menu' : get_menu,
		'cart' : cart,
	}

	return render(request, 'shop/catalog_brand.html', context)

def show_product_card(request, sub_category, product):
	try:
		cart_id = request.session['cart_id']
		cart = Card.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Card()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Card.objects.get(id=cart_id)

	
	product = Product.objects.get(slug=product, is_active=True)
	image_list = product.images.all()
	get_menu = Menu.objects.all()

	context = {
		'products' : product,
		'get_menu' : get_menu,
		'cart' : cart,
		'image_list': image_list
	}

	return render(request, 'shop/product_page.html', context)

def shop_page(request, category, brand):
	try:
		cart_id = request.session['cart_id']
		cart = Card.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Card()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Card.objects.get(id=cart_id)

	cat_ = category
	categorys = Menu.objects.filter(slug=category)
	model_phones = ModelPhone.objects.all()

	get_menu = Menu.objects.all()
	get_cat = Category.objects.get(slug=brand)
	get_menu_category = Menu.objects.get(slug=category)

	products = Product.objects.filter(menu=get_menu_category, category=get_cat, is_active=True)
	products_all = Product.objects.filter(menu=get_menu_category, category=get_cat, is_active=True)

	ajax_true = request.GET.get('ajax')

	paginator = Paginator(products, 9)
	page = request.GET.get('page')

	if ajax_true == 'True':
		order_by = request.GET.get('order_by')

		if order_by == 'price':
			products = products.order_by('price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
			request.session['order_by'] = 'price'
		elif order_by == 'price-desc':
			products = products.order_by('-price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
			request.session['order_by'] = 'price-desc'
		elif order_by == 'create_date':
			products = products.order_by('create_date')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
			request.session['order_by'] = 'create_date'

		return JsonResponse({
			'html': render_to_string("shop/include/item_in_shop.html", {'products': products})
			})

	try:
		order_by = request.session['order_by']

		if order_by == 'price':
			products = products.order_by('price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
		elif order_by == 'price-desc':
			products = products.order_by('-price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
		elif order_by == 'create_date':
			products = products.order_by('create_date')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
	except:
		pass

	products = paginator.get_page(page)

	context = {
		'products' : products,
		'categorys' : categorys,
		'model_phones' : model_phones,
		'get_menu' : get_menu,
		'cat_' : cat_,
		'cart' : cart,
		'brand': brand,
		'p_count' : len(products_all)
	}
	return	render(request, 'shop/shop_page.html', context)

def shop_page_model(request, category, brand, product):
	try:
		cart_id = request.session['cart_id']
		cart = Card.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Card()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Card.objects.get(id=cart_id)

	
	cat_ = category
	categorys = Menu.objects.filter(slug=category)
	model_phones = ModelPhone.objects.all()

	get_menu_all = Menu.objects.all()

	get_menu = Menu.objects.get(slug=category)
	get_cat = Category.objects.get(slug=brand)
	get_mp = ModelPhone.objects.get(slug=product)

	products = Product.objects.filter(menu=get_menu, category=get_cat, model_phone=get_mp, is_active=True)
	products_all = Product.objects.filter(menu=get_menu, category=get_cat, is_active=True)

	ajax_true = request.GET.get('ajax')

	paginator = Paginator(products, 9)
	page = request.GET.get('page')

	if ajax_true == 'True':
		order_by = request.GET.get('order_by')

		if order_by == 'price':
			products = products.order_by('price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
			request.session['order_by'] = 'price'
		elif order_by == 'price-desc':
			products = products.order_by('-price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
			request.session['order_by'] = 'price-desc'
		elif order_by == 'create_date':
			products = products.order_by('create_date')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
			request.session['order_by'] = 'create_date'

		return JsonResponse({
			'html': render_to_string("shop/include/item_in_shop.html", {'products': products})
			})

	try:
		order_by = request.session['order_by']

		if order_by == 'price':
			products = products.order_by('price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
		elif order_by == 'price-desc':
			products = products.order_by('-price')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
		elif order_by == 'create_date':
			products = products.order_by('create_date')
			paginator = Paginator(products, 9)
			products = paginator.get_page(page)
	except:
		pass

	products = paginator.get_page(page)
	
	context = {
		'products' : products,
		'categorys' : categorys,
		'model_phones' : model_phones,
		'get_menu_all' : get_menu_all,
		'cat_' : cat_,
		'get_menu' : get_menu_all,
		'cart' : cart,
		'brand': product,
		'p_count' : len(products_all)
	}

	return	render(request, 'shop/shop_page.html', context)


def add_to_cart_view(request):
	request_id = request.GET.get('poduct_id')

	try:
		cart_id = request.session['cart_id']
		cart = Card.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Card()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Card.objects.get(id=cart_id)
	product = Product.objects.get(id=request_id)

	cart.add_to_cart(product.id)

	total_price = 0

	for item in cart.items.all():
		total_price += item.item_total

	cart.cart_total = total_price
	cart.save()

	return JsonResponse({
		'cart_total': cart.items.count(), 
		'total_price': cart.cart_total, 
		'html': render_to_string("shop/include/item_in_b.html", {'cart': cart})
		})

def remove_from_cart_view(request):
	cart_id = request.session['cart_id']
	request_id_item = request.GET.get('poduct_id')

	cart = Card.objects.get(id=cart_id)
	product = Product.objects.get(id=request_id_item)

	cart.remove_from_cart(product.id)

	total_price = 0

	for item in cart.items.all():
		total_price += item.item_total

	cart.cart_total = total_price
	cart.save()

	return JsonResponse({
		'cart_total': cart.items.count(), 
		'total_price': cart.cart_total, 
		'html': render_to_string("shop/include/item_in_b.html", {'cart': cart})
		})

def checkout(request):
	get_menu_all = Menu.objects.all()

	try:
		cart_id = request.session['cart_id']
	except:
		return render(request, 'shop/checkout.html' )

	cart = Card.objects.get(id=cart_id)

	context = {
		'cart': cart,
		'get_menu' : get_menu_all,
	}

	return render(request, 'shop/checkout.html', context)

def buy(request):
	cart_id = request.session['cart_id']

	cart = Card.objects.get(id=cart_id)

	if request.method == "POST":
		order = Order()
		order.save()

		order.name = request.POST.get('name')
		order.last_name = request.POST.get('last_name')
		order.city = request.POST.get('city')
		order.new_poch = request.POST.get('new_poch')
		order.phone = request.POST.get('phone')
		order.total_price = cart.cart_total

		for item in cart.items.all():
			p_item = PropertyOrder()
			p_item.object = item.product
			p_item.order = order
			p_item.save()
		
		order.save()

		del request.session['cart_id']
		
		return JsonResponse({'status': '200'})
	else:
		return JsonResponse({'status': '0'})

def buy_one_click(request):
	cart_id = request.session['cart_id']

	cart = Card.objects.get(id=cart_id)

	if request.method == "POST":
		order = Order()
		order.save()

		order.phone = request.POST.get('phone')
		order.total_price = cart.cart_total
		order.status = 'ONECLICK'

		for item in cart.items.all():
			p_item = PropertyOrder()
			p_item.object = item.product
			p_item.order = order
			p_item.save()
			# order.items.add(item)
		
		order.save()
		
		del request.session['cart_id']

		return JsonResponse({'status': '200'})
	else:
		return JsonResponse({'status': '0'})

def buy_one_click_one(request):

	get_item_id = request.POST.get('product_id')

	if request.method == "POST":
		order = Order()
		order.save()

		cart = Card()
		cart.save()

		cart_id = cart.id
		cart = Card.objects.get(id=cart_id)

		product = Product.objects.get(id=get_item_id)

		cart.add_to_cart(product.id)

		total_price = 0

		for item in cart.items.all():
			total_price += item.item_total

		cart.cart_total = total_price

		cart.save()

		order.phone = request.POST.get('phone')
		order.total_price = cart.cart_total
		order.status = 'ONECLICK'

		for item in cart.items.all():
			p_item = PropertyOrder()
			p_item.object = item.product
			p_item.order = order
			p_item.save()
			# order.items.add(item)
		
		order.save()
		
		return JsonResponse({'status': '200'})
	else:
		return JsonResponse({'status': '0'})
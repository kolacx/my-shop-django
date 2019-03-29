from django.contrib import admin
import decimal
from django.utils.html import format_html
from django.template.loader import render_to_string
from .models import Product, Category, ModelPhone, Menu, CartItem, Card, Order, PropertyImage, MainPage, PropertyOrder

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyOrderInline(admin.TabularInline):
    model = PropertyOrder
    extra = 1

@admin.register(Product)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]
    list_display = ('head_title', 'id', 'is_active', 'in_sale', 'is_new', 'price', 'sale_price')
    list_filter = ('is_active', 'in_sale', 'is_new',)
    # list_editable = ('is_active', 'in_sale', 'is_new',)

admin.site.register(Category)
admin.site.register(ModelPhone)
admin.site.register(Menu)
# admin.site.register(CartItem)
# admin.site.register(Card)
admin.site.register(MainPage)
# admin.site.register(Order)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'status', 'comment', 'cross_prod', 'all_price')
	list_filter = ('status',)
	list_editable = ('status', )
	inlines = [ PropertyOrderInline, ]

	def all_price(self, obj):

		# order = obj.total_price
		# total = 0.00

		try:
			order_cross = obj.ooo.all()
			cross_price = 0.00
			for i in order_cross:
				if i.object.in_sale == True:
					cross_price = decimal.Decimal(cross_price) + i.object.sale_price
				else:
					cross_price = decimal.Decimal(cross_price) + i.object.price
			# total = order + cross_price
		except:
			cross_price = cross_price

		return cross_price

	# def get_products(self, obj):
	# 	return format_html(render_to_string("order/admin/items.html", {'card': obj}))

	def cross_prod(self, obj):
		return format_html(render_to_string("order/admin/items_cross.html", {'card': obj}))
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from shop.models import Product, Menu

class ProductSitemap(Sitemap):

    def items(self):
        return Product.objects.all()


class MenuSitemap(Sitemap):

	def items(self):
		return Menu.objects.all()

class StaticViewSitemap(Sitemap):

	def items(self):
		return ['shop:delivery_url']

	def location(self, item):
	    return reverse(item)
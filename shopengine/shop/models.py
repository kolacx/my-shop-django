from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class MainPage(models.Model):
	head_image = models.ImageField(upload_to='products')
	sub_head_text = models.CharField(max_length=200, verbose_name='Подзаголовок', blank=True)
	head_text = models.CharField(max_length=200, verbose_name='Заголовок', blank=True)
	url_button = models.URLField(max_length=200, verbose_name='Ссылка в кнопку')
	text_btn = models.CharField(max_length=200, verbose_name='Текст кнопки')

	is_active_sale = models.BooleanField(default=False, verbose_name='Есть ли распродажа?')
	sale_img = models.ImageField(upload_to='products')
	percent = models.CharField(max_length=200, verbose_name='Процент скидки', blank=True)
	text = models.CharField(max_length=200, verbose_name='Заголовок распродажи', blank=True)
	btn_sale = models.URLField(max_length=200, verbose_name='Ссылка в кнопку распродажи', blank=True)
	text_btn_sale = models.CharField(max_length=200, verbose_name='Текст кнопки скидки', default='Текст кнопки скидки')

	class Meta:
		verbose_name = "Главная страница"
		verbose_name_plural = "Главная страница"

def image_folder(instance, filename):
	filename = instance.slug + '.' + filename.split('.')[1]
	return "{0}/{1}".format(instance.slug, filename)

class Product(models.Model):
	is_active = models.BooleanField(default=True, verbose_name='Доступный товар?')
	in_sale = models.BooleanField(default=False, verbose_name='Учавствует в распродаже?')
	is_new = models.BooleanField(default=False, verbose_name='Новый товар?')
	head_title = models.CharField(max_length=200, verbose_name='Заголовок')
	price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
	sale_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена с Скидкой', blank=True, default=0.00)
	menu = models.ForeignKey('Menu', verbose_name='К какой категории?', on_delete=models.CASCADE, blank=True, null=True)
	category = models.ForeignKey('Category', verbose_name='Бренд', on_delete=models.CASCADE)
	model_phone = models.ForeignKey('ModelPhone', verbose_name='Модель', on_delete=models.CASCADE)
	specifications = RichTextField(verbose_name='Характеристики', blank=True)
	properties = RichTextField(verbose_name='Свойства', blank=True)
	image = models.ImageField(upload_to='products')


	create_date = models.DateTimeField(auto_now_add=True, null=True)

	slug = AutoSlugField(populate_from='head_title', unique=True, db_index=True, editable=True, blank=True)

	def __str__(self):
		return self.head_title
    	
	class Meta:
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"

	def get_absolute_url(self):
		return reverse('shop:show_product_card_urls', kwargs={'sub_category' : self.model_phone.slug, 'product':self.slug})

class PropertyImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

class Menu(models.Model):
	title = models.CharField(max_length=100, verbose_name='Название категории')
	what_brand = models.ManyToManyField('Category', verbose_name="Какие категории сюда входят?", blank=True)
	image = models.ImageField(upload_to='products', null=True)

	slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=True, blank=True)


	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def get_absolute_url(self):
		return reverse('shop:shop_page_model_url', kwargs={'slug':self.slug})

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=100, verbose_name='Название бренда')
	phone_models = models.ManyToManyField('ModelPhone', verbose_name="Какие модели сюда входят?")
	image = models.ImageField(upload_to='products', null=True)

	slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=True, blank=True)

	def __str__(self):
		return self.title
	   	
	class Meta:
		verbose_name = "Бренд"
		verbose_name_plural = "Бренды"

	def get_absolute_url(self):
		return reverse('shop:product_page_url', kwargs={'slug':self.slug})

class ModelPhone(models.Model):
	title = models.CharField(max_length=100, verbose_name="Модель телефона")
	slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=True, blank=True)

	def __str__(self):
		return self.title
	   	
	class Meta:
		verbose_name = "Модель"
		verbose_name_plural = "Модели"

	def get_absolute_url(self):
		return reverse('shop:product_page_url', kwargs={'brand' : Category.slug, 'product' : self.slug})


class CartItem(models.Model):

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	qty = models.PositiveIntegerField(default=1)
	item_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

	def __str__(self):
		return self.product.head_title


class Card(models.Model):

	items = models.ManyToManyField(CartItem, blank=True)
	cart_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

	def __str__(self):
		return str(self.id)

	def add_to_cart(self, product_id):
		cart = self
		product = Product.objects.get(id=product_id)

		if product.in_sale == True:
			new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.sale_price)
		else:
			new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)

		if new_item not in cart.items.all():
			cart.items.add(new_item)
			cart.save()

	def remove_from_cart(self, product_id):
		cart = self
		product = Product.objects.get(id=product_id)

		for cart_item in cart.items.all():
			if cart_item.product == product:
				cart.items.remove(cart_item)
				cart.save()



class Order(models.Model):
	ORDER_STATES = (
	    ("Создан", ("Создан")),
	    ("ONECLICK", ("One Click")),
	    ("Подтвержденный", ("Подтвержденный")),
	    ("В Обработке", ("В обработке")),
	    ("Отменен", ("Отменен")),
	    ("Отправлен", ("Отправлен"))
	)

	name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=True)
	phone = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=500, blank=True)
	new_poch = models.CharField(max_length=500, default='', blank=True)

	items = models.ManyToManyField(CartItem, blank=True)

	total_price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

	status = models.CharField(max_length=200, choices=ORDER_STATES, default='Создан')

	comment = RichTextField(verbose_name='Комент', blank=True)

	def __str__(self):
		return 'Заказ № {0}'.format(str(self.id))

	class Meta:
		verbose_name = "Заказы"
		verbose_name_plural = "Заказы"

class PropertyOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ooo')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    object = GenericForeignKey('content_type', 'object_id')
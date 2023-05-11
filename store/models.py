from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	number_phone =models.CharField(max_length=17)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.email

'''
class ProductImage(models.Model):
    prddname = models.CharField(max_length=55)
    prdimg = models.ImageField(upload_to='img_prd/')

    def __str__(self):
        return self.prodname
def img_def(instence, filename):
    imagename, extention = filename.split((','))
    return 'product/%s.%s'%(instence.id,extention)
'''
@ receiver(post_save, sender=User)
def create_user_customer(sender, instance, created,**kwargs):
	if created:
		Customer.objects.create(
			user=instance
		)


class Product(models.Model):
	name = models.CharField(max_length=66, unique=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
	author = models.CharField(max_length=55, default='admin')
	description = models.TextField(default='This Is A Description For Product', max_length=150)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	is_stock = models.BooleanField()
	is_active = models.BooleanField()
	digital = models.BooleanField(default=False, null=True, blank=True)
	category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	stock = models.CharField(max_length=6, null=True, blank=True)

	slug = models.SlugField(null=True, blank=True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'
		ordering = ('-date_created',)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address


class Category(models.Model):
    category = models.CharField(max_length=55)
    date_add = models.DateTimeField(auto_now=True)
    catimg = models.ImageField(upload_to='static/staticfiles/',verbose_name='categryImage')
    slug = models.SlugField(max_length=55, null=True, blank=True)

    class Meta:

        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category


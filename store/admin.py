from django.contrib import admin

from .models import *
from .models import Product, Customer, Order, OrderItem, ShippingAddress, Category


class AdminCategory(admin.ModelAdmin):

    list_display = ('category','date_add')


class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email')


class AdminOrder(admin.ModelAdmin):
    list_display =['customer']


class AdminOrderItem(admin.ModelAdmin):
    list_display = ('product', 'quantity')


class AdminShippingAddress(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city', 'state', 'zipcode')


class AdminProduct(admin.ModelAdmin):

    list_display = ('name', 'price', 'slug', 'author', 'stock', 'is_stock', 'date_created', )
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ["name", "price", "is_stock", 'is_active']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, AdminOrder)

admin.site.register(OrderItem, AdminOrderItem)
admin.site.register(ShippingAddress, AdminShippingAddress)


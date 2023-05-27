from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'store'

urlpatterns = [
    path('', views.store, name="store"),
    path('mybase/', views.mybase, name="mybase"),
    path('mydetail/', views.mydetail, name="mydetail"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:product_id>/', views.detail, name="detail"),
]

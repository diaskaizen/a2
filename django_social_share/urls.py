from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'social'

urlpatterns = [
    path('social/', views.home, name="social"),
    #path('product/<int:product_id>/', views.detail, name="detail"),

]

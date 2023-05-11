from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('api/', views.api_conf, name='api'),
    path('profile/', views.profile, name='profile'),
    path('status/', views.status, name='status'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/', views.customer, name='customer'),
    path('customer/<str:pk_t>/', views.customer, name='customer'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

]

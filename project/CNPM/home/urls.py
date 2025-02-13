from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name='login'),
    path('thucan/', views.thucan, name='thucan'),
    path('home/', views.Customer, name='Customer'),
    path('home/', views.Veterinarian, name='Veterinarian'),
    path('api/revenue/', views.revenue_api, name='revenue_api'),
]
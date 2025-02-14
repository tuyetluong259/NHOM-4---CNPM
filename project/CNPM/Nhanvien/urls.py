from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_NV, name = 'home_NV'),
    path('booking/', views.booking, name='booking'),
    path('pet/', views.pet, name='pet'),
    path('schedule/', views.schedule, name='schedule'),
    path('room/', views.room, name='room'),
    path('login/', views.login, name='login'),
    
]
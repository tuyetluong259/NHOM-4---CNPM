from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'), 
    path('thucan/', views.thucan, name='thucan'),
    path('customer/', views.Customer, name='customer'),
    path('veterinarian/', views.Veterinarian, name='veterinarian'),
    path('login/', LoginView.as_view(), name='login'),  # Đổi thành login_view
]

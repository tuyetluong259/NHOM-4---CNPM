from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='get_home'),  # Trang chính
    path('bang/', views.bang_view, name='bang'),  # Trang bang
]


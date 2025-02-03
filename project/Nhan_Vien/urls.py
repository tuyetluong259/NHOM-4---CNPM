from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.list_phong, name='list_phong'),
    path('pets/', views.list_thucung, name='list_thucung'),
    path('bookings/', views.list_booking, name='list_booking'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('schedule/', views.list_lichkham, name='list_lichkham'),
]

# staff/urls.py

from django.urls import path
from .views import homepage, kennel_list, add_kennel, edit_kennel, delete_kennel, booking_list, cancel_booking, pet_admission_list, add_pet_admission, vet_schedule_list, add_vet_schedule

urlpatterns = [
    # Danh sách chuồng
    path('kennel/', kennel_list, name='kennel_list'),
    # Thêm chuồng
    path('kennel/add/', add_kennel, name='add_kennel'),
    # Sửa chuồng
    path('kennel/edit/<int:pk>/', edit_kennel, name='edit_kennel'),
    # Xóa chuồng
    path('kennel/delete/<int:pk>/', delete_kennel, name='delete_kennel'),
    
    # Danh sách booking
    path('booking/', booking_list, name='booking_list'),
    # Hủy booking
    path('booking/cancel/<int:pk>/', cancel_booking, name='cancel_booking'),
    
    # Danh sách pet admissions
    path('pet_admission/', pet_admission_list, name='pet_admission_list'),
    # Thêm pet admission
    path('pet_admission/add/', add_pet_admission, name='add_pet_admission'),
    
    # Danh sách vet schedules
    path('vet_schedule/', vet_schedule_list, name='vet_schedule_list'),
    # Thêm vet schedule
    path('vet_schedule/add/', add_vet_schedule, name='add_vet_schedule'),
    
    # Trang chủ
    path('http://127.0.0.1:8000/admin', homepage, name='homepage'),

]

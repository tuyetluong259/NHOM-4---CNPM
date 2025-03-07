from django.urls import path
from .views import list_bookings, cancel_booking
from . import views 
urlpatterns = [
    path('', views.home_NV, name='home_NV'),  # Trang chủ Nhân viên
    path("booking/", list_bookings, name="list_bookings"),  # Đảm bảo đặt name="list_bookings"
    path("booking/cancel/<int:booking_id>/", cancel_booking, name="cancel_booking"),
    path('schedule/', views.schedule, name='schedule'),  # Quản lý lịch khám của bác sĩ
    path('add_schedule/', views.add_schedule, name='add_schedule'),  # Thêm mới lịch khám
    path('pet/', views.pet, name='pet'),  # Quản lý thú cưng nhập viện
    path('add_pet/', views.add_pet, name='add_pet'),  # Thêm hồ sơ nhập viện cho thú cưng
    path('room/', views.room, name='room'),  # Quản lý phòng khám
    path('add_room/', views.add_room, name='add_room'),  # Thêm mới phòng khám
    path('login/', views.login, name='login'),  # Đăng nhập
]
"""path('booking/', views.booking, name='booking'),  # Quản lý đặt lịch khám
    path('add_booking/', views.add_booking, name='add_booking'),  # Thêm mới đặt lịch khám"""
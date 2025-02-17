from django.contrib import admin
from django.urls import path
from . import views
from home.views import revenue_dashboard, revenue_api, myadmin_view

urlpatterns = [
    # 🌐 Trang chủ
    path('', views.home, name="home"),

    # 📊 Trang admin tùy chỉnh
    path("myadmin/", myadmin_view, name="custom-admin-home"),

    # 📊 API
    path('api/revenue/', revenue_api, name='revenue_api'),
    path('admin/revenue-dashboard/', revenue_dashboard, name='revenue-dashboard'),

    # 🔐 Authentication
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    # 🏠 Home theo vai trò
    path('homeBS/', views.homeBS, name='homeBS'),
    path('homeNV/', views.homeNV, name='homeNV'),
    path('homeKH/', views.homeKH, name='homeKH'),

    # 📅 Booking & Lịch trình
    path('bookings/', views.bookings, name='bookings'),
    path('schedule/', views.schedule, name='schedule'),

    # 🏥 Quản lý thú cưng & y tế
    path('quan_ly_thu_cung/', views.quan_ly_thu_cung, name='quan_ly_thu_cung'),
    path('record_medical/', views.record_medical, name='record_medical'),
    path('edit_medical/', views.edit_medical, name='edit_medical'),
    path('dang_ky_kham_benh/', views.dang_ky_kham_benh, name='dang_ky_kham_benh'),
    path('inpatient_care/', views.inpatient_care, name='inpatient_care'),

    # 🐶 Dịch vụ & Chi tiết thú cưng
    path('thucan/', views.thucan, name='thucan'),
    path('pets/', views.pets, name='pets'),
    path('chi_tiet_thu_cung/', views.chi_tiet_thu_cung, name='chi_tiet_thu_cung'),

    # 📢 Đánh giá & hỗ trợ khách hàng
    path('danh_gia_nguoi_dung/', views.danh_gia_nguoi_dung, name='danh_gia_nguoi_dung'),
    path('giao_dien_khach_hang/', views.giao_dien_khach_hang, name='giao_dien_khach_hang'),

    # 🏠 Giao diện chính
    path('index/', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
]

from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
   path('', views.home, name='home'),
    path('quan-ly-thu-cung/', views.quan_ly_thu_cung, name='quan_ly_thu_cung'),
     path('chi-tiet-thu-cung/', views.chi_tiet_thu_cung, name='chi_tiet_thu_cung'),
    path('dang-ky-kham-benh/', views.dang_ky_kham_benh, name='dang_ky_kham_benh'),
    path('danh-gia-nguoi-dung/', views.danh_gia_nguoi_dung, name='danh_gia_nguoi_dung'),
    path('thong-tin-khac/', views.thong_tin_khac, name='thong_tin_khac'),
     path('giao_dien_khach_hang/', views.giao_dien_khach_hang, name='giao_dien_khach_hang'),
]
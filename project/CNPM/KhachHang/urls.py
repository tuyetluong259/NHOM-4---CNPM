from django.urls import path
from .import views  # Corrected the import statement

urlpatterns = [
    path('', views.home, name='home'),
    path('quan-ly-thu-cung/', views.quan_ly_thu_cung, name='quan_ly_thu_cung'),
    path('dang-ky-kham-benh/', views.dang_ky_kham_benh, name='dang_ky_kham_benh'),
    path('danh-gia-nguoi-dung/', views.danh_gia_nguoi_dung, name='danh_gia_nguoi_dung'),
    path('quan-ly-lich-hen/', views.quan_ly_lich_hen, name='quan_ly_lich_hen'),
    path('giao_dien_khach_hang/', views.giao_dien_khach_hang, name='giao_dien_khach_hang'),
    path('login/', views.login, name='login'),
]

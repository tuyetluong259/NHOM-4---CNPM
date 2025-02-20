from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('record_medical/', views.record_medical, name='record_medical'),  # Trang ghi nhận hồ sơ
    path('inpatient_care/', views.inpatient_care, name='inpatient_care'),  # Trang chăm sóc thú cưng
    path('edit_medical/<int:pk>/', views.edit_medical, name='edit_medical'),  # Trang sửa hồ sơ
    path('login/', views.login, name='login'),
    path('delete_medical/<int:pk>/', views.delete_medical, name='delete_medical'),  # Xóa hồ sơ
]

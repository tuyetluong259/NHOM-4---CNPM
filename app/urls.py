from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('record_medical/', views.record_medical, name='record_medical'),  # Trang ghi nhận hồ sơ
    path('inpatient_care/', views.inpatient_care, name='inpatient_care'),  # Trang chăm sóc thú cưng
]

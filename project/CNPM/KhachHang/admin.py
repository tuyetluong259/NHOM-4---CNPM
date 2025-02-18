# KhachHang/admin.py
from django.contrib import admin
from .models import Category, Customer  # Đảm bảo bạn đã import đúng

admin.site.register(Category)  # Đăng ký model Category
admin.site.register(Customer)  # Đăng ký model Customer

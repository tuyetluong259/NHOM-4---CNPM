from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
# from import_export.admin import ExportMixin
from import_export.admin import ExportMixin
from .models import SystemConfig, Revenue
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def revenue_dashboard(request):
    # Kiểm tra xem user có phải là staff hay không (để bảo vệ trang admin)
    if not request.user.is_staff:
        return redirect('/admin/login/?next=/admin/revenue-dashboard/')
    return render(request, 'admin/myadmin.html')

# Bạn có thể tạo một danh sách URL tùy chỉnh cho dashboard
admin_urls = [
    path('revenue-dashboard/', revenue_dashboard, name='revenue-dashboard'),
]

class MyAdminSite(admin.AdminSite):
    # Bạn có thể tùy biến các thuộc tính này nếu muốn
    site_header = "My Custom Admin"
    site_title = "My Admin"
    index_title = "Welcome to My Admin"

    def get_urls(self):
        """Khai báo thêm một URL tùy chỉnh 'my-dashboard/'"""
        urls = super().get_urls()
        custom_urls = [
            path('my-dashboard/', self.admin_view(self.my_dashboard_view), name='my-dashboard'),
        ]
        return custom_urls + urls

    def my_dashboard_view(self, request):
        """
        Hàm view hiển thị template tùy chỉnh.
        - @admin_view tự động kiểm tra user có quyền truy cập admin không.
        """
        return render(request, 'admin/myadmin.html', {})

# Tạo một thể hiện AdminSite
my_admin_site = MyAdminSite(name='myadmin')

# (Tùy chọn) Đăng ký các model tại đây, thay vì admin.site.register
# from .models import YourModel
# my_admin_site.register(YourModel)
class SystemConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key',)

class RevenueAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('date', 'amount')
    list_filter = ('date',)
    search_fields = ('date',)
    ordering = ('-date',)

admin.site.register(SystemConfig, SystemConfigAdmin)
admin.site.register(Revenue, RevenueAdmin)
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
  list_display = ("full_name", "phone_number", "address",)
  
class VeterinarianAdmin(admin.ModelAdmin):
  list_display = ("staff", "specialty", "available_times",)
  


# class SystemConfigAdmin(admin.ModelAdmin):
#     list_display = ('key', 'value')
#     search_fields = ('key',)

# class RevenueAdmin(ExportMixin, admin.ModelAdmin):
#     list_display = ('date', 'amount')
#     list_filter = ('date',)
#     search_fields = ('date',)
#     ordering = ('-date',)

# admin.site.register(SystemConfig, SystemConfigAdmin)
# admin.site.register(Revenue, RevenueAdmin)
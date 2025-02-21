from django.contrib import admin
from .models import Customer, Veterinarian
# from import_export.admin import ExportMixin

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
  list_display = ("full_name", "phone_number", "address",)
  
class VeterinarianAdmin(admin.ModelAdmin):
  list_display = ("staff", "specialty", "available_times",)
  
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Veterinarian, VeterinarianAdmin)


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
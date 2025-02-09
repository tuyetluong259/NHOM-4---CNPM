from django.contrib import admin
from .models import Customer, Veterinarian
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
  list_display = ("full_name", "phone_number", "address",)
  
class VeterinarianAdmin(admin.ModelAdmin):
  list_display = ("staff", "specialty", "available_times",)
  
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Veterinarian, VeterinarianAdmin)


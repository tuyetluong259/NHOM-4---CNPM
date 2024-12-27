from django.contrib import admin
from .models import Kennel, Booking, PetAdmission, VetSchedule

# Đăng ký các models vào admin site
admin.site.register(Kennel)
admin.site.register(Booking)
admin.site.register(PetAdmission)
admin.site.register(VetSchedule)

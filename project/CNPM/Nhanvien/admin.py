from django.contrib import admin
from .models import Booking, PetHospitalization, DoctorSchedule, Room

admin.site.register(Booking)
admin.site.register(PetHospitalization)
admin.site.register(DoctorSchedule)
admin.site.register(Room)

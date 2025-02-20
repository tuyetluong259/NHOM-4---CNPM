from django.db import models
from django.utils.timezone import now

class Booking(models.Model):
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    pet_name = models.CharField(max_length=255, null=True, blank=True)
    pet_gender = models.CharField(max_length=10, null=True, blank=True)
    pet_condition = models.TextField(null=True, blank=True)

    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)

    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    staff_notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(default=now)  # Thêm giá trị mặc định

    def __str__(self):
        return f"{self.pet_name or 'Unknown'} - {self.owner_name or 'Unknown'}"

class PetHospitalization(models.Model):
    pet_name = models.CharField(max_length=100, null=True, blank=True)
    diagnosis = models.TextField(default='Unknown diagnosis', null=True, blank=True)
    admission_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.pet_name or 'Unknown Pet'} - {self.diagnosis}"

class DoctorSchedule(models.Model):
    doctor_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.doctor_name or 'Unknown Doctor'} - {self.date or 'No Date'} - {self.time or 'No Time'}"
    
class Room(models.Model):
    room_number = models.CharField(max_length=10, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Room {self.room_number or 'Unknown'} - Capacity: {self.capacity or 'Unknown'}"

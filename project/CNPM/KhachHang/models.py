from django.db import models

class Appointment(models.Model):
    owner_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    
    pet_name = models.CharField(max_length=255)
    pet_gender = models.CharField(max_length=10)
    pet_condition = models.TextField()
    
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    
    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    staff_notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet_name} - {self.owner_name}"

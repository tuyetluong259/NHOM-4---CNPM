from django.db import models

class Appointment(models.Model):
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    pet_name = models.CharField(max_length=255, null=True, blank=True)
    pet_gender = models.CharField(max_length=10, null=True, blank=True)
    pet_condition = models.TextField(null=True, blank=True)

    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)

    doctor_name = models.CharField(max_length=255, null=True, blank=True)
    staff_notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)


    def __str__(self):
        return f"{self.pet_name or 'Unknown Pet'} - {self.owner_name or 'Unknown Owner'}"

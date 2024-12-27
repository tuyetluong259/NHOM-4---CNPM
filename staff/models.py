# staff/models.py

from django.db import models

class Kennel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Booking(models.Model):
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=255)
    booking_date = models.DateTimeField()

class PetAdmission(models.Model):
    pet_name = models.CharField(max_length=255)
    admission_date = models.DateTimeField()
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)

class VetSchedule(models.Model):
    pet_admission = models.ForeignKey(PetAdmission, on_delete=models.CASCADE)
    vet_name = models.CharField(max_length=255)
    schedule_date = models.DateTimeField()

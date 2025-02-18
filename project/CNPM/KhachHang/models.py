# KhachHang/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
    
class Registration(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    pet_name = models.CharField(max_length=255)
    pet_gender = models.CharField(max_length=10, choices=[('Male', 'Đực'), ('Female', 'Cái')])
    pet_condition = models.TextField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    doctor_choice = models.CharField(max_length=255, choices=[
        ('Bác sĩ Triệu Hoàng Nam', 'Bác sĩ Triệu Hoàng Nam'),
        ('Tiến sĩ Nguyễn Văn A', 'Tiến sĩ Nguyễn Văn A'),
        ('Bác sĩ Nguyễn Văn Hùng', 'Bác sĩ Nguyễn Văn Hùng'),
        ('Bác sĩ Võ Hùng', 'Bác sĩ Võ Hùng')
    ])
    
    def __str__(self):
        return self.full_name


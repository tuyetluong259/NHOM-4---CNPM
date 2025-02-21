from django.db import models
from django.utils.timezone import now

class Booking(models.Model):
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    pet_name = models.CharField(max_length=255, null=True, blank=True)
    pet_species = models.CharField(max_length=100, null=True, blank=True)  # Thêm cột loài vật nuôi
    pet_gender = models.CharField(max_length=10, null=True, blank=True)
    pet_condition = models.TextField(null=True, blank=True)
    cage_number = models.IntegerField(null=True, blank=True)

    appointment_date = models.DateField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)

    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    staff_notes = models.TextField(blank=True, null=True)

    # Các trường bổ sung từ MedicalRecord
    STATUS_CHOICES = [
        ('NHAP_VIEN', 'Nhập viện'),
        ('XUAT_VIEN', 'Xuất viện'),
        ('DIEU_TRI', 'Đang điều trị'),
        ('CHUA_DIEU_TRI', 'Chưa điều trị'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='CHUA_DIEU_TRI'
    )
    diagnosis = models.TextField(null=True, blank=True)
    prescription = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(default=now)

    # Cột trạng thái thanh toán
    is_paid = models.BooleanField(default=True)  # False = chưa thanh toán, True = đã thanh toán

    # Cột phí khám cố định
    fee_amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=200000.00  # Cố định phí khám là 200,000 VND
    )

    def __str__(self):
        return f"{self.pet_name or 'Unknown'} - {self.pet_species or 'Unknown'} - {self.owner_name or 'Unknown'} - {'Đã thanh toán' if self.is_paid else 'Chưa thanh toán'}"

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

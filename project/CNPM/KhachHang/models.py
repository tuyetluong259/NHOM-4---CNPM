from django.db import models
from django.utils.timezone import now

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
        default='CHUA_DIEU_TRI'  # Giá trị mặc định là 'Đang điều trị'
    )
    diagnosis = models.TextField(null=True, blank=True)
    prescription = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(default=now)  # Thêm giá trị mặc định

    def __str__(self):
        return f"{self.pet_name or 'Unknown'} - {self.owner_name or 'Unknown'}"

from django.db import models  
from Nhanvien.models import Booking  # Liên kết với Booking nếu có

class MedicalRecord(models.Model):
    booking = models.ForeignKey(
        Booking, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="medical_records"  # Giúp truy vấn dễ dàng từ Booking
    )
    STATUS_CHOICES = [
        ('NHAP_VIEN', 'Nhập viện'),
        ('XUAT_VIEN', 'Xuất viện'),
        ('DIEU_TRI', 'Đang điều trị'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DIEU_TRI'  # Giá trị mặc định là 'Đang điều trị'
    )
    doctor_name = models.CharField(max_length=255, null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    prescription = models.TextField(null=True, blank=True)
    cage_number = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.booking.pet_name if self.booking else 'Unknown'}"

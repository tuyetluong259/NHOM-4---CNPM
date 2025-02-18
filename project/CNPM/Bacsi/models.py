from django.db import models

class MedicalRecord(models.Model):
    patient_name = models.CharField(max_length=255, default='Chưa có tên')  # Tên thú cưng
    diagnosis = models.TextField(default='Chưa có chẩn đoán')  # Chẩn đoán
    progress = models.CharField(max_length=100)  # Tiến trình điều trị
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày giờ tạo hồ sơ

    def __str__(self):
        return self.patient_name

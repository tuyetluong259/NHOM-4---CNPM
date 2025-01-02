from django.db import models

class MedicalRecord(models.Model):
    name = models.CharField(max_length=100)  # Tên thú cưng
    species = models.CharField(max_length=100)  # Loài thú cưng
    progress = models.CharField(max_length=255)  # Tiến trình điều trị
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo hồ sơ

    def __str__(self):
        return self.name  # Trả về tên thú cưng khi hiển thị

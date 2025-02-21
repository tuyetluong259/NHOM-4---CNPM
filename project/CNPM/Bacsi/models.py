from django.db import models

class MedicalRecord(models.Model):
    # Các trường dữ liệu của mô hình này
    patient_name = models.CharField(max_length=100)
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    progress = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name

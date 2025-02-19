from django.db import models

# Mô hình khách hàng
class KhachHang(models.Model):
    owner_name = models.CharField(max_length=255, null=True, blank=True)  # Họ tên chủ thú cưng
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Số điện thoại
    email = models.EmailField(unique=True, null=True, blank=True)  # Email
    address = models.CharField(max_length=255, null=True, blank=True)  # Địa chỉ

    def __str__(self):
        return self.owner_name

# Mô hình thú cưng
class ThuCung(models.Model):
    GIOI_TINH_CHOICES = [
        ('male', 'Đực'),
        ('female', 'Cái'),
    ]

    pet_name = models.CharField(max_length=255, null=True, blank=True)  # Tên thú cưng
    pet_gender = models.CharField(max_length=10, choices=GIOI_TINH_CHOICES, null=True, blank=True)  # Giới tính thú cưng
    pet_condition = models.TextField(null=True, blank=True)  # Mô tả tình trạng
    owner = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name="thu_cung", null=True, blank=True)  # Chủ sở hữu

    def __str__(self):
        return f"{self.pet_name} - {self.owner.owner_name if self.owner else 'Không rõ'}"

# Mô hình bác sĩ
class BacSi(models.Model):
    ten = models.CharField(max_length=100, null=True, blank=True)  # Tên bác sĩ

    def __str__(self):
        return self.ten if self.ten else 'Không rõ'

# Mô hình lịch hẹn khám
class LichHen(models.Model):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE, null=True, blank=True)  # Khách hàng
    thu_cung = models.ForeignKey(ThuCung, on_delete=models.SET_NULL, null=True, blank=True)  # Thú cưng
    appointment_date = models.DateField(null=True, blank=True)  # Ngày hẹn
    appointment_time = models.TimeField(null=True, blank=True)  # Giờ hẹn
    bac_si = models.ForeignKey(BacSi, on_delete=models.SET_NULL, null=True, blank=True)  # Bác sĩ
    staff_notes = models.TextField(null=True, blank=True)  # Ghi chú

    def __str__(self):
        return f"Lịch hẹn: {self.thu_cung.pet_name if self.thu_cung else 'Không rõ'} - {self.appointment_date} {self.appointment_time}"

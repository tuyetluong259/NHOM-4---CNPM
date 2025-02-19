from django.db import models

# Mô hình khách hàng
class KhachHang(models.Model):
    owner_name = models.CharField(max_length=255)  # Họ tên chủ thú cưng
    phone_number = models.CharField(max_length=15)  # Số điện thoại
    email = models.EmailField(unique=True)  # Email
    address = models.CharField(max_length=255)  # Địa chỉ

    def __str__(self):
        return self.owner_name

# Mô hình thú cưng
class ThuCung(models.Model):
    GIOI_TINH_CHOICES = [
        ('male', 'Đực'),
        ('female', 'Cái'),
    ]

    pet_name = models.CharField(max_length=255)  # Tên thú cưng
    pet_gender = models.CharField(max_length=10, choices=GIOI_TINH_CHOICES)  # Giới tính thú cưng
    pet_condition = models.TextField()  # Mô tả tình trạng
    owner = models.ForeignKey(KhachHang, on_delete=models.CASCADE, related_name="thu_cung")  # Chủ sở hữu

    def __str__(self):
        return f"{self.pet_name} - {self.owner.owner_name}"

# Mô hình bác sĩ
class BacSi(models.Model):
    doctor_name = models.CharField(max_length=255)  # Họ tên bác sĩ

    def __str__(self):
        return self.doctor_name

# Mô hình lịch hẹn khám
class LichHen(models.Model):
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)  # Tham chiếu đến khách hàng
    thu_cung = models.ForeignKey(ThuCung, on_delete=models.CASCADE)  # Tham chiếu đến thú cưng
    appointment_date = models.DateField()  # Ngày hẹn
    appointment_time = models.TimeField()  # Giờ hẹn
    doctor_name = models.CharField(
        max_length=255,
        choices=[
            ('Triệu Hoàng Nam', 'Bác sĩ Triệu Hoàng Nam'),
            ('Phạm Thảo', 'Tiến sĩ Phạm Thảo'),
            ('Nguyễn Văn Hùng', 'Bác sĩ Nguyễn Văn Hùng'),
            ('Võ Hùng', 'Bác sĩ Võ Hùng'),
            ('Bùi Minh Tân', 'Bác sĩ Bùi Minh Tân'),
            ('Võ Hạnh Nhi', 'Bác sĩ Võ Hạnh Nhi'),
        ],
        blank=True,
        null=True
    )  # Bác sĩ được chọn từ danh sách hoặc để trống
    staff_notes = models.TextField(blank=True, null=True)  # Ghi chú cho nhân viên

    def __str__(self):
        return f"Lịch hẹn: {self.thu_cung.pet_name} - {self.appointment_date} {self.appointment_time}"

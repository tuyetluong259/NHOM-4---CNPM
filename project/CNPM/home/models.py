from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
class SystemConfig(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

class Revenue(models.Model):
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.date}: {self.amount}"

# Model Thú cưng
class ThuCung(models.Model):
    ten = models.CharField(max_length=100)
    loai = models.CharField(max_length=100)
    tuoi = models.IntegerField()
    chu = models.ForeignKey(User, on_delete=models.CASCADE)
    ngay_tao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ten

# Model Hồ sơ khám bệnh của Thú cưng
class HoSoKhamBenh(models.Model):
    thu_cung = models.ForeignKey(ThuCung, on_delete=models.CASCADE)
    ngay_kham = models.DateTimeField()
    chuan_doan = models.TextField()
    dieu_tri = models.TextField()
    danh_gia = models.IntegerField(choices=[(1, 'Rất Tệ'), (2, 'Tệ'), (3, 'Bình Thường'), (4, 'Tốt'), (5, 'Rất Tốt')], null=True, blank=True)

    def __str__(self):
        return f"Hồ sơ khám bệnh của {self.thu_cung.ten} vào ngày {self.ngay_kham}"

# Model Chuồng (phòng) cho thú cưng nhập viện
class ChungCu(models.Model):
    ma_chuong = models.CharField(max_length=100, unique=True)
    loai_chuong = models.CharField(max_length=100)
    trang_thai = models.BooleanField(default=True)

    def __str__(self):
        return f"Chuồng {self.ma_chuong} - {'Trống' if self.trang_thai else 'Đầy'}"

# Model Đặt khám bệnh (booking)

def some_default_user():
    try:
        user = User.objects.get(username='default_user')  # Lấy người dùng có tên 'default_user'
        return user.id  # Trả về id của user
    except User.DoesNotExist:
        # Nếu không tồn tại, tạo người dùng mặc định
        user = User.objects.create_user(username='default_user', password='password123')
        return user.id

def some_default_thu_cung():
    # Đảm bảo rằng có một user mặc định để gán cho trường 'chu'
    default_owner = User.objects.get(username='default_user')
    # Lấy thú cưng đầu tiên nếu có
    thu_cung = ThuCung.objects.first()
    if not thu_cung:
        thu_cung = ThuCung.objects.create(
            ten='Thú cưng mặc định', 
            loai='Loại mặc định',
            tuoi=0,  # Cung cấp giá trị mặc định cho 'tuoi'
            chu=default_owner  # Gán chủ nhân mặc định
        )
    return thu_cung.id
class Booking(models.Model):
    thu_cung = models.ForeignKey(ThuCung, on_delete=models.CASCADE, default=some_default_thu_cung)
    khach_hang = models.ForeignKey(User, on_delete=models.CASCADE, default=some_default_user)
    ngay_dang_ky = models.DateTimeField(auto_now_add=True, null=True)
    bac_si = models.ForeignKey('BacSi', null=True, blank=True, on_delete=models.SET_NULL)
    trang_thai = models.CharField(
        max_length=50, 
        choices=[('Đang Chờ', 'Đang Chờ'), ('Đã Xác Nhận', 'Đã Xác Nhận'), ('Đã Hủy', 'Đã Hủy')],
        default='Đang Chờ'
    )
    thanh_toan_truoc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"Booking cho {self.thu_cung.ten} vào ngày {self.ngay_dang_ky}"

# Model Bác sĩ thú y
class BacSi(models.Model):
    ten = models.CharField(max_length=100)
    chuyen_mon = models.CharField(max_length=100)
    gioi_thieu = models.TextField()
    trang_thai = models.BooleanField(default=True)

    def __str__(self):
        return self.ten

# Model Thông tin tài khoản người dùng
class TaiKhoan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    loai_tai_khoan = models.CharField(max_length=50, choices=[('Khách Hàng', 'Khách Hàng'), ('Nhân Viên', 'Nhân Viên'), ('Admin', 'Admin'), ('Bác Sĩ', 'Bác Sĩ')])
    so_dien_thoai = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Model Cấu hình hệ thống
class CauHinh(models.Model):
    ten = models.CharField(max_length=100)
    gia_tri = models.CharField(max_length=100)
    mo_ta = models.TextField()

    def __str__(self):
        return self.ten

# Model Doanh thu hệ thống
class DoanhThu(models.Model):
    thoi_gian = models.DateField()
    doanh_thu_ngay = models.DecimalField(max_digits=10, decimal_places=2)
    doanh_thu_tuan = models.DecimalField(max_digits=10, decimal_places=2)
    doanh_thu_thang = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Doanh thu ngày {self.thoi_gian}"

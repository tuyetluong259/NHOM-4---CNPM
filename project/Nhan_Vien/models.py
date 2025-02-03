from django.db import models

# Quản lý nhân viên
class NhanVien(models.Model):
    ten = models.CharField(max_length=100)
    email = models.EmailField()
    so_dien_thoai = models.CharField(max_length=15)
    dia_chi = models.TextField()

    def __str__(self):
        return self.ten

# Quản lý phòng (chuồng)
class Phong(models.Model):
    ten_phong = models.CharField(max_length=100)
    loai_phong = models.CharField(max_length=50)
    suc_chua = models.IntegerField()

    def __str__(self):
        return self.ten_phong

# Quản lý thú cưng
class ThuCung(models.Model):
    ten = models.CharField(max_length=100)
    loai = models.CharField(max_length=50)
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

# Quản lý booking
class Booking(models.Model):
    ten_thu_cung = models.CharField(max_length=100)
    chu_so_huu = models.CharField(max_length=100)
    trang_thai = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.ten_thu_cung} - {self.trang_thai}"

# Quản lý lịch bác sĩ thú y
class LichKham(models.Model):
    ten_thu_cung = models.CharField(max_length=100)
    ten_bac_si = models.CharField(max_length=100)
    thoi_gian = models.DateTimeField()

    def __str__(self):
        return f"{self.ten_thu_cung} - {self.ten_bac_si}"

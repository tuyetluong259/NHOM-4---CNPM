from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

def get_default_user():
    user, created = User.objects.get_or_create(username="default_user", defaults={"email": "default@example.com"})
    return user.id

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

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=get_default_user)
    phone = models.CharField(max_length=15, unique=True, default='0000000000')
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Pet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.species})"

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.name} - {self.date}"

class Invoice(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for {self.appointment.pet.name} on {self.issued_at}"

class Review(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.appointment.pet.name} - {self.rating}/5"

class BacSi(models.Model):
    ten = models.CharField(max_length=100)
    chuyen_mon = models.CharField(max_length=100)
    gioi_thieu = models.TextField()
    trang_thai = models.BooleanField(default=True)

    def __str__(self):
        return self.ten

class ChungCu(models.Model):
    ma_chuong = models.CharField(max_length=100, unique=True)
    loai_chuong = models.CharField(max_length=100)
    trang_thai = models.BooleanField(default=True)

    def __str__(self):
        return f"Chuồng {self.ma_chuong} - {'Trống' if self.trang_thai else 'Đầy'}"

class CauHinh(models.Model):
    ten = models.CharField(max_length=100)
    gia_tri = models.CharField(max_length=100)
    mo_ta = models.TextField()

    def __str__(self):
        return self.ten

class DoanhThu(models.Model):
    thoi_gian = models.DateField()
    doanh_thu_ngay = models.DecimalField(max_digits=10, decimal_places=2)
    doanh_thu_tuan = models.DecimalField(max_digits=10, decimal_places=2)
    doanh_thu_thang = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Doanh thu ngày {self.thoi_gian}"

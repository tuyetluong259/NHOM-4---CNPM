from django.db import models

# Mô hình cho Booking (Đặt lịch khám)
class Booking(models.Model):
    pet_name = models.CharField(max_length=100, default='Unknown')  # Thêm giá trị mặc định
    owner_name = models.CharField(max_length=255, default='Unknown')
    appointment_date = models.DateTimeField(null=True)  # Thêm giá trị mặc định
    # Các trường khác nếu có

    def __str__(self):
        return f"{self.pet_name} - {self.owner_name} - {self.appointment_date}"

class PetHospitalization(models.Model):
    pet_name = models.CharField(max_length=100)
    diagnosis = models.TextField(default='Unknown diagnosis')  # Cung cấp giá trị mặc định
    admission_date = models.DateTimeField()

    def __str__(self):
        return f"{self.pet_name} - {self.diagnosis}"


    def __str__(self):
        return f"{self.pet_name} - {self.diagnosis}"

# Mô hình cho DoctorSchedule (Lịch khám bác sĩ

class DoctorSchedule(models.Model):
    doctor_name = models.CharField(max_length=100)
    date = models.DateField(null=True)  # Cho phép trường 'date' có giá trị null
    time = models.TimeField(null=True)  # Cho phép trường 'time' có giá trị null

    def __str__(self):
        return f"{self.doctor_name} - {self.date} - {self.time}"
    

# Mô hình cho Room (Phòng khám)
class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Room {self.room_number} - Capacity: {self.capacity}"

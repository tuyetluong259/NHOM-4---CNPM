from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now

# Model để lưu thông tin log
class Log(models.Model):
    ACTION_CHOICES = [
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted'),
    ]
    model_name = models.CharField(max_length=255)  # Tên model (Booking, PetHospitalization, DoctorSchedule, Room)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)  # Hành động: tạo, sửa, xóa
    object_id = models.PositiveIntegerField()  # ID của đối tượng bị thay đổi
    details = models.TextField()  # Thông tin chi tiết về đối tượng
    timestamp = models.DateTimeField(auto_now_add=True)  # Thời gian thực hiện hành động

    def __str__(self):
        return f"{self.model_name} - {self.action} at {self.timestamp}"

# Model Quản lý Booking
class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')])

    def __str__(self):
        return f"{self.customer_name} - {self.room}"

# Model Quản lý thú cưng nhập viện
class PetHospitalization(models.Model):
    pet_name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    cage_number = models.IntegerField()
    admission_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('under_treatment', 'Under Treatment'), ('discharged', 'Discharged')])

    def __str__(self):
        return f"{self.pet_name} - {self.owner_name}"

# Model Sắp lịch Bác Sĩ
class DoctorSchedule(models.Model):
    doctor_name = models.CharField(max_length=255)
    schedule_time = models.DateTimeField()
    room = models.CharField(max_length=255)
    schedule_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.doctor_name} - {self.schedule_time}"

# Model Quản lý chuồng
class Room(models.Model):
    room_name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('occupied', 'Occupied')])

    def __str__(self):
        return f"{self.room_name} - {self.room_type}"

# Hàm lưu log sau khi tạo hoặc cập nhật
@receiver(post_save, sender=Booking)
def save_booking_log(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    Log.objects.create(
        model_name='Booking',
        action=action,
        object_id=instance.id,
        details=f"Customer: {instance.customer_name}, Room: {instance.room}, Amount: {instance.amount}, Status: {instance.status}"
    )

@receiver(post_save, sender=PetHospitalization)
def save_pet_hospitalization_log(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    Log.objects.create(
        model_name='PetHospitalization',
        action=action,
        object_id=instance.id,
        details=f"Pet: {instance.pet_name}, Owner: {instance.owner_name}, Cage: {instance.cage_number}, Status: {instance.status}"
    )

@receiver(post_save, sender=DoctorSchedule)
def save_doctor_schedule_log(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    Log.objects.create(
        model_name='DoctorSchedule',
        action=action,
        object_id=instance.id,
        details=f"Doctor: {instance.doctor_name}, Schedule Time: {instance.schedule_time}, Room: {instance.room}, Type: {instance.schedule_type}"
    )

@receiver(post_save, sender=Room)
def save_room_log(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    Log.objects.create(
        model_name='Room',
        action=action,
        object_id=instance.id,
        details=f"Room: {instance.room_name}, Type: {instance.room_type}, Status: {instance.status}"
    )

# Hàm lưu log sau khi xóa
@receiver(post_delete, sender=Booking)
def delete_booking_log(sender, instance, **kwargs):
    Log.objects.create(
        model_name='Booking',
        action='deleted',
        object_id=instance.id,
        details=f"Customer: {instance.customer_name}, Room: {instance.room}, Amount: {instance.amount}, Status: {instance.status}"
    )

@receiver(post_delete, sender=PetHospitalization)
def delete_pet_hospitalization_log(sender, instance, **kwargs):
    Log.objects.create(
        model_name='PetHospitalization',
        action='deleted',
        object_id=instance.id,
        details=f"Pet: {instance.pet_name}, Owner: {instance.owner_name}, Cage: {instance.cage_number}, Status: {instance.status}"
    )

@receiver(post_delete, sender=DoctorSchedule)
def delete_doctor_schedule_log(sender, instance, **kwargs):
    Log.objects.create(
        model_name='DoctorSchedule',
        action='deleted',
        object_id=instance.id,
        details=f"Doctor: {instance.doctor_name}, Schedule Time: {instance.schedule_time}, Room: {instance.room}, Type: {instance.schedule_type}"
    )

@receiver(post_delete, sender=Room)
def delete_room_log(sender, instance, **kwargs):
    Log.objects.create(
        model_name='Room',
        action='deleted',
        object_id=instance.id,
        details=f"Room: {instance.room_name}, Type: {instance.room_type}, Status: {instance.status}"
    )

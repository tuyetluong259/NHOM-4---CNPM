from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import MedicalRecord
from Nhanvien.models import Booking  # Import Booking

# Tự động tạo MedicalRecord khi có Booking mới
@receiver(post_save, sender=Booking)
def create_Bacsi(sender, instance, created, **kwargs):
    if created and not MedicalRecord.objects.filter(booking=instance).exists():
        print(f"🔹 Creating MedicalRecord for Booking {instance.id}")
        MedicalRecord.objects.create(
            booking=instance,
            doctor_name=instance.doctor_name
        )

# Cập nhật MedicalRecord khi Booking thay đổi
@receiver(post_save, sender=Booking)
def update_Bacsi(sender, instance, **kwargs):
    print(f"🔹 Updating MedicalRecord for Booking {instance.id}")
    try:
        Bacsi = MedicalRecord.objects.get(booking=instance)
        Bacsi.doctor_name = instance.doctor_name
        Bacsi.save()
    except MedicalRecord.DoesNotExist:
        pass  # Không làm gì nếu MedicalRecord không tồn tại

# Xóa MedicalRecord khi Booking bị xóa
@receiver(pre_delete, sender=Booking)
def delete_Bacsi(sender, instance, **kwargs):
    print(f"🔹 Deleting MedicalRecord for Booking {instance.id}")
    MedicalRecord.objects.filter(booking=instance).delete()

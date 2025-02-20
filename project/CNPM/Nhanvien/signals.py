from django.db.models.signals import post_save, post_delete, pre_delete

from django.dispatch import receiver
from KhachHang.models import Appointment
from Nhanvien.models import Booking
from Bacsi.models import MedicalRecord

# Cờ bảo vệ để tránh vòng lặp vô hạn
prevent_recursion = False
@receiver(post_save, sender=Booking)
def create_medical_record(sender, instance, created, **kwargs):
    if created:
        MedicalRecord.objects.create(
            booking=instance,
            doctor_name=instance.doctor_name  # Lấy thông tin bác sĩ từ Booking
        )

@receiver(post_save, sender=Booking)
def update_medical_record_from_booking(sender, instance, **kwargs):
    if hasattr(instance, 'medical_record'):
        medical_record = instance.medical_record
        medical_record.doctor_name = instance.doctor_name  # Cập nhật tên bác sĩ
        medical_record.save()

@receiver(pre_delete, sender=Booking)
def delete_medical_record_with_booking(sender, instance, **kwargs):
    if hasattr(instance, 'medical_record'):
        instance.medical_record.delete()


@receiver(post_save, sender=Appointment)
def sync_appointment_to_booking(sender, instance, **kwargs):
    global prevent_recursion
    if prevent_recursion:
        return  # Ngăn vòng lặp vô hạn

    prevent_recursion = True
    Booking.objects.update_or_create(
        phone_number=instance.phone_number,
        defaults={
            'owner_name': instance.owner_name,
            'email': instance.email,
            'address': instance.address,
            'pet_name': instance.pet_name,
            'pet_gender': instance.pet_gender,
            'pet_condition': instance.pet_condition,
            'appointment_date': instance.appointment_date,
            'appointment_time': instance.appointment_time,
            'doctor_name': instance.doctor_name,
            'staff_notes': instance.staff_notes
        }
    )
    prevent_recursion = False  # Reset cờ sau khi cập nhật xong

@receiver(post_save, sender=Booking)
def sync_booking_to_appointment(sender, instance, **kwargs):
    global prevent_recursion
    if prevent_recursion:
        return

    prevent_recursion = True
    Appointment.objects.update_or_create(
        phone_number=instance.phone_number,
        defaults={
            'owner_name': instance.owner_name,
            'email': instance.email,
            'address': instance.address,
            'pet_name': instance.pet_name,
            'pet_gender': instance.pet_gender,
            'pet_condition': instance.pet_condition,
            'appointment_date': instance.appointment_date,
            'appointment_time': instance.appointment_time,
            'doctor_name': instance.doctor_name,
            'staff_notes': instance.staff_notes
        }
    )
    prevent_recursion = False

@receiver(post_delete, sender=Appointment)
def delete_booking_when_appointment_deleted(sender, instance, **kwargs):
    Booking.objects.filter(phone_number=instance.phone_number).delete()

@receiver(post_delete, sender=Booking)
def delete_appointment_when_booking_deleted(sender, instance, **kwargs):
    Appointment.objects.filter(phone_number=instance.phone_number).delete()

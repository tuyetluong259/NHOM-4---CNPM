from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import MedicalRecord
from Nhanvien.models import Booking

# Cờ bảo vệ vòng lặp
prevent_recursion = False

@receiver(post_save, sender=Booking)
def sync_booking_to_medical_record(sender, instance, **kwargs):
    """Đồng bộ Booking -> MedicalRecord"""
    global prevent_recursion
    if prevent_recursion:
        return
    
    prevent_recursion = True
    MedicalRecord.objects.update_or_create(
        booking=instance,
        defaults={
            'doctor_name': instance.doctor_name,
            'status': instance.status,
            'diagnosis': instance.diagnosis,
            'prescription': instance.prescription,
            'notes': instance.notes
        }
    )
    prevent_recursion = False

@receiver(post_save, sender=MedicalRecord)
def sync_medical_record_to_booking(sender, instance, **kwargs):
    """Đồng bộ MedicalRecord -> Booking"""
    global prevent_recursion
    if prevent_recursion:
        return
    
    prevent_recursion = True
    booking = instance.booking
    booking.doctor_name = instance.doctor_name
    booking.status = instance.status
    booking.diagnosis = instance.diagnosis
    booking.prescription = instance.prescription
    booking.notes = instance.notes
    booking.save()
    prevent_recursion = False

@receiver(pre_delete, sender=Booking)
def delete_medical_record_with_booking(sender, instance, **kwargs):
    """Xóa MedicalRecord khi Booking bị xóa"""
    MedicalRecord.objects.filter(booking=instance).delete()

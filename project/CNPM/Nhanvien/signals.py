from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from KhachHang.models import Appointment
from Nhanvien.models import Booking
from Bacsi.models import MedicalRecord

# Cờ bảo vệ để tránh vòng lặp vô hạn
prevent_recursion = False

### 🏥 1. Đồng bộ Booking với MedicalRecord
@receiver(post_save, sender=Booking)
def sync_medical_record(sender, instance, created, **kwargs):
    """Tạo hoặc cập nhật MedicalRecord khi Booking thay đổi"""
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
            'notes': instance.notes,
            'cage_number': instance.cage_number  # Thêm số phòng
        }
    )
    prevent_recursion = False

@receiver(pre_delete, sender=Booking)
def delete_medical_record_with_booking(sender, instance, **kwargs):
    """Xóa MedicalRecord khi Booking bị xóa"""
    if hasattr(instance, 'medical_record'):
        instance.medical_record.delete()

### 📅 2. Đồng bộ Appointment với Booking
@receiver(post_save, sender=Appointment)
def sync_appointment_to_booking(sender, instance, **kwargs):
    """Đồng bộ Appointment -> Booking"""
    global prevent_recursion
    if prevent_recursion:
        return

    prevent_recursion = True
    Booking.objects.update_or_create(
        id=instance.id,  # Sử dụng ID thay vì phone_number để tránh nhầm bản ghi
        defaults={ 
            'owner_name': instance.owner_name,
            'phone_number': instance.phone_number,  # Đảm bảo giữ số điện thoại
            'email': instance.email,
            'address': instance.address,
            'pet_name': instance.pet_name,
            'pet_species': instance.pet_species,
            'pet_gender': instance.pet_gender,
            'pet_condition': instance.pet_condition,
            'appointment_date': instance.appointment_date,
            'appointment_time': instance.appointment_time,
            'doctor_name': instance.doctor_name,
            'staff_notes': instance.staff_notes,
            'is_paid': instance.is_paid,
            'fee_amount': instance.fee_amount,
        }
    )
    prevent_recursion = False

@receiver(post_save, sender=Booking)
def sync_booking_to_appointment(sender, instance, **kwargs):
    """Đồng bộ Booking -> Appointment"""
    global prevent_recursion
    if prevent_recursion:
        return

    prevent_recursion = True
    Appointment.objects.update_or_create(
        id=instance.id,  # Sử dụng ID thay vì phone_number
        defaults={
            'owner_name': instance.owner_name,
            'phone_number': instance.phone_number,
            'email': instance.email,
            'address': instance.address,
            'pet_name': instance.pet_name,
            'pet_gender': instance.pet_gender,
            'pet_condition': instance.pet_condition,
            'appointment_date': instance.appointment_date,
            
            'appointment_time': instance.appointment_time,
            'doctor_name': instance.doctor_name,
            'staff_notes': instance.staff_notes,
            'status': instance.status,
            'diagnosis': instance.diagnosis,
            'prescription': instance.prescription,
            'notes': instance.notes
        }
    )
    prevent_recursion = False

### 🗑️ 3. Xóa Booking hoặc Appointment khi một trong hai bị xóa
@receiver(post_delete, sender=Appointment)
def delete_booking_when_appointment_deleted(sender, instance, **kwargs):
    """Xóa Booking khi Appointment bị xóa"""
    Booking.objects.filter(id=instance.id).delete()  # Dùng ID để tránh xóa nhầm

@receiver(post_delete, sender=Booking)
def delete_appointment_when_booking_deleted(sender, instance, **kwargs):
    """Xóa Appointment khi Booking bị xóa"""
    Appointment.objects.filter(id=instance.id).delete()

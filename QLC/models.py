from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('RR', 'Room Regular'),
        ('DB', 'Deluxe Room'),
        ('TC', 'Tiny Cage'),
    ]
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)
    status = models.CharField(max_length=20, default='Available')  # Status: Available, Occupied, etc.
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Lưu thông tin khách hàng
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.BooleanField(default=False)  # Thanh toán: True (đã thanh toán), False (chưa thanh toán)

    def __str__(self):
        return f"Booking {self.id} by {self.customer.username} for Room {self.room.room_number}"

    def cancel_booking(self):
        if self.status != 'Cancelled':
            self.status = 'Cancelled'
            self.save()

            # Nếu đã thanh toán, hoàn tiền
            if self.payment_status:
                self.refund_payment()

    def refund_payment(self):
        # Logic hoàn tiền
        print(f"Refunding {self.total_price} to {self.customer.username}")

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Liên kết với khách hàng

    def __str__(self):
        return self.name


class Admission(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Admitted')  # Admitted, Discharged

    def __str__(self):
        return f"{self.pet.name} in Room {self.room.room_number}"

class Vet(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    is_walk_in = models.BooleanField(default=False)  # True if walk-in, False if pre-booked

    def __str__(self):
        return f"Appointment for {self.pet.name} with Dr. {self.vet.name} on {self.appointment_date}"


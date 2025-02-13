from django.db import models

#class
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    def __str__(self):
        return self.full_name
    
class Pet(models.Model):
    customer = models.ForeignKey(Customer, related_name="pets", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.TextField()
    vaccine_history = models.TextField()
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=50) 
    def __str__(self):
        return self.full_name
    
class Veterinarian(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    available_times = models.TextField()  # Thời gian bác sĩ có thể làm việc
    def __str__(self):
        return f"Dr. {self.staff.full_name}"
    
class Booking(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')])
    payment_status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Booking for {self.pet.name} on {self.date}"
    
class Admission(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('In Hospital', 'In Hospital'), ('Recovered', 'Recovered')])
    notes = models.TextField()
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    def __str__(self):
        return f"Admission for {self.pet.name} on {self.check_in_date}"
    
class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField()
    def __str__(self):
        return f"Review for {self.booking.pet.name} by {self.customer.full_name}"
    
class Revenue(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    revenue_type = models.CharField(max_length=50, choices=[('Booking', 'Booking'), ('Service', 'Service'), ('Refund', 'Refund')])
    def __str__(self):
        return f"Revenue on {self.date}: {self.amount}"
    
# class SystemConfig(models.Model):
#     key = models.CharField(max_length=255, unique=True)
#     value = models.TextField()

#     def __str__(self):
#         return self.key

# class Revenue(models.Model):
#     date = models.DateField(default=now)
#     amount = models.DecimalField(max_digits=12, decimal_places=2)

#     def __str__(self):
#         return f"{self.date}: {self.amount}"
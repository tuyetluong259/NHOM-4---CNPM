# staff/views.py

from django.shortcuts import render, redirect
from .models import Kennel, Booking, PetAdmission, VetSchedule

# Danh sách chuồng
def kennel_list(request):
    kennels = Kennel.objects.all()
    return render(request, 'staff/kennel_list.html', {'kennels': kennels})

# Thêm chuồng
def add_kennel(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        new_kennel = Kennel(name=name, description=description)
        new_kennel.save()
        return redirect('kennel_list')
    return render(request, 'staff/add_kennel.html')

# Sửa chuồng
def edit_kennel(request, pk):
    kennel = Kennel.objects.get(pk=pk)
    if request.method == 'POST':
        kennel.name = request.POST['name']
        kennel.description = request.POST['description']
        kennel.save()
        return redirect('kennel_list')
    return render(request, 'staff/edit_kennel.html', {'kennel': kennel})

# Xóa chuồng
def delete_kennel(request, pk):
    kennel = Kennel.objects.get(pk=pk)
    kennel.delete()
    return redirect('kennel_list')

# Danh sách booking
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'staff/booking_list.html', {'bookings': bookings})

# Hủy booking
def cancel_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.status = 'Cancelled'
    booking.save()
    return redirect('booking_list')

# Danh sách pet admissions
def pet_admission_list(request):
    admissions = PetAdmission.objects.all()
    return render(request, 'staff/pet_admission_list.html', {'admissions': admissions})

# Thêm pet admission
def add_pet_admission(request):
    if request.method == 'POST':
        pet_name = request.POST['pet_name']
        kennel = Kennel.objects.get(pk=request.POST['kennel'])
        admission_date = request.POST['admission_date']
        new_admission = PetAdmission(pet_name=pet_name, admission_date=admission_date, kennel=kennel)
        new_admission.save()
        return redirect('pet_admission_list')
    kennels = Kennel.objects.all()
    return render(request, 'staff/add_pet_admission.html', {'kennels': kennels})

# Danh sách vet schedules
def vet_schedule_list(request):
    schedules = VetSchedule.objects.all()
    return render(request, 'staff/vet_schedule_list.html', {'schedules': schedules})

# Thêm vet schedule
def add_vet_schedule(request):
    if request.method == 'POST':
        pet_admission = PetAdmission.objects.get(pk=request.POST['pet_admission'])
        vet_name = request.POST['vet_name']
        schedule_date = request.POST['schedule_date']
        new_schedule = VetSchedule(pet_admission=pet_admission, vet_name=vet_name, schedule_date=schedule_date)
        new_schedule.save()
        return redirect('vet_schedule_list')
    pet_admissions = PetAdmission.objects.all()
    return render(request, 'staff/add_vet_schedule.html', {'pet_admissions': pet_admissions})





def homepage(request):
    return render(request, 'staff/homepage.html')


# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking, PetHospitalization, DoctorSchedule, Room

# Create your views here.
def home_NV(request):
    return render(request, 'Nhanvien/home_NV.html')

def booking(request):
    bookings = Booking.objects.all()
    return render(request, 'Nhanvien/booking.html', {'bookings': bookings})

def schedule(request):
    schedules = DoctorSchedule.objects.all()
    return render(request, 'Nhanvien/schedule.html', {'schedules': schedules})

def pet(request):
    pets = PetHospitalization.objects.all()
    return render(request, 'Nhanvien/pet.html', {'pets': pets})

def room(request):
    rooms = Room.objects.all()
    return render(request, 'Nhanvien/room.html', {'rooms': rooms})

def login(request):
    return render(request, 'home/login.html')

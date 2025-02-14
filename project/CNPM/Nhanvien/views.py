from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_NV(request):
    return render(request,'Nhanvien/home_NV.html')
def booking(request):
    return render(request, 'Nhanvien/booking.html')
def schedule(request):
    return render(request, 'Nhanvien/schedule.html')
def pet(request):
    return render(request, 'Nhanvien/pet.html')
def room(request):
    return render(request, 'Nhanvien/room.html')
def login(request):
    return render(request, 'home/login.html')

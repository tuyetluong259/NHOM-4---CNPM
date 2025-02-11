from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_NV(request):
    return render(request,'app/home_NV.html')
def booking(request):
    return render(request, 'app/booking.html')
def schedule(request):
    return render(request, 'app/schedule.html')
def pet(request):
    return render(request, 'app/pet.html')
def room(request):
    return render(request, 'app/room.html')
def login(request):
    return render(request, 'app/login.html')

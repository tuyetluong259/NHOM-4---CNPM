from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'app/home.html')
def booking(request):
    return render(request, 'app/booking.html')
def schedule(request):
    return render(request, 'app/schedule.html')
def pet(request):
    return render(request, 'app/pet.html')
def room(request):
    return render(request, 'app/room.html')
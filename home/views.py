from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home page!")

def bang_view(request):
    return HttpResponse("Đây là trang bang!")
def get_home(request):
    return render(request, 'home.html')
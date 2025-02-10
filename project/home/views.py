from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages

# Trang chủ
def home(request):
    return render(request, 'home/home.html')

# Trang thức ăn
def thucan(request):
    return render(request, 'home/thucan.html')

# Trang khách hàng
def Customer(request):
    return render(request, 'customer.html')

# Trang bác sĩ thú y
def Veterinarian(request):
    return render(request, 'veterinarian.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):  
    return render(request, 'home/login.html')

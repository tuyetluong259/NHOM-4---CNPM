from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home (request):
    context = {}
    return render(request, 'home/home.html', context)
def login(request):
    context = {}
    return render(request, 'home/login.html', context)
def thucan(request):
    context = {}
    return render(request, 'home/thucan.html', context)
def index(request):
    return render(request, 'index.html')  # Tên file template là 'index.html'
# Create your views here.
def Customer(request):
    return HttpResponse("Hello world!") 
def Veterinarian(request):
    return HttpResponse("Hello world!")

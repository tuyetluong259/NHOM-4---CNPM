from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request, 'home/home.html')

# Create your views here.
def Customer(request):
    return HttpResponse("Hello world!") 
def Veterinarian(request):
    return HttpResponse("Hello world!")
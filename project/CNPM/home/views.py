from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Revenue

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
def 
# Create your views here.
def Customer(request):
    return HttpResponse("Hello world!") 
def Veterinarian(request):
    return HttpResponse("Hello world!")

def revenue_api(request):
    revenues = Revenue.objects.order_by('date')
    data = {
        "dates": [r.date.strftime("%Y-%m-%d") for r in revenues],
        "amounts": [float(r.amount) for r in revenues]
    }
    return JsonResponse(data)

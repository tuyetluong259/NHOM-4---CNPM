from django.http import JsonResponse
from .models import Revenue
from django.shortcuts import render

def revenue_api(request):
    revenues = Revenue.objects.order_by('date')
    data = {
        "dates": [r.date.strftime("%Y-%m-%d") for r in revenues],
        "amounts": [float(r.amount) for r in revenues]
    }
    return JsonResponse(data)


def revenue_dashboard(request):
    return render(request, 'admin/revenue_dashboard.html')

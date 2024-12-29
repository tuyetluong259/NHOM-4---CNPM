from django.shortcuts import render

def room_list(request):
    return render(request, 'your_app/room_list.html')

# Create your views here.

# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('staff.urls')),  # Bao gồm các URL của app staff
]

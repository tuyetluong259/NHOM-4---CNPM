from django import forms
from .models import Appointment  # Đảm bảo model mới đã được import đúng

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment  # Sử dụng model mới
        fields = '__all__'  # Hoặc liệt kê các trường cụ thể nếu cần 
        
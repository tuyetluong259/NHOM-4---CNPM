from django import forms
from .models import LichHen

class LichHenForm(forms.ModelForm):
    class Meta:
        model = LichHen
        fields = ['khach_hang', 'thu_cung', 'appointment_date', 'appointment_time', 'doctor_name', 'staff_notes']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

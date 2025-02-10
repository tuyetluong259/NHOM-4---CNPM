from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'room_type', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }

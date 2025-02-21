from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pet_name', 'pet_species', 'status', 'doctor_name', 'is_paid', 'cage_number']
        widgets = {
            'pet_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pet_species': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=Booking.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cage_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
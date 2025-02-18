from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'phone_number', 'email', 'address', 'pet_name', 
                  'pet_gender', 'pet_condition', 'appointment_date', 'appointment_time', 'doctor_choice']

from django import forms
from .models import KhachHang, ThuCung, LichHen, BacSi

class KhachHangForm(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = ['owner_name', 'phone_number', 'email', 'address']

class ThuCungForm(forms.ModelForm):
    class Meta:
        model = ThuCung
        fields = ['pet_name', 'pet_gender', 'pet_condition']

class LichHenForm(forms.ModelForm):
    class Meta:
        model = LichHen
        fields = ['appointment_date', 'appointment_time', 'bac_si', 'staff_notes']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

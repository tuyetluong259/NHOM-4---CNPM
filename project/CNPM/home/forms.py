from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Mật khẩu')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = get_user_model().objects.get(email=email)
            return user
        except get_user_model().DoesNotExist:
            raise forms.ValidationError("Không tìm thấy tài khoản với email này.")

from django import forms
from .models import CustomUser

class SignupForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    district = forms.CharField(max_length=100)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'phone', 'country', 'city', 'district']
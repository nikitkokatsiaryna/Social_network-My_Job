from django import forms
from .models import Users


class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
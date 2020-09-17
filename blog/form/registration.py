from django import forms
from ..models import User, Profile
from django.contrib.auth.password_validation import validate_password


# class LoginForm(forms.Form):
#     user_name = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=5)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput, min_length=5)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('password1', error)
        return password1


class SignUpForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']
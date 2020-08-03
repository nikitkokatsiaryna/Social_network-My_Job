from django import forms
from django.forms import ModelForm
from .models import Experience, Education


class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExperienceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Experience
        fields = {"position"}
        # fields = '__all__'
        employment_choices = (
            # ('Empty', '-'),
            ('FD', 'Full work day'),
            ('PE', 'Partial employment'),
            ('BM', 'Businessman'),
            ('F', 'Freelance'),
            ('C', 'Contract'),
            ('I', 'Internship'),
        )
        widgets = {
            'type_employment': forms.Select(choices=employment_choices, attrs={'class': 'form-control'}),
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-control'})
        }

        labels = {
            'position': 'Должность',
            'type_employment': 'Тип занятости',
            'company': 'Компания',
            'region': 'Регион',
            'date_start': 'Дата начала',
            'date_end': 'Дата окончания',
            'description': 'Описание',
        }


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Education
        fields = {'institution'}
        # fields = "__all__"

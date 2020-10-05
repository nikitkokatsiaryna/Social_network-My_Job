from django import forms
from ..models import Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ('user',)

        widgets = {
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-calendar'}, years=range(1900, 2100)),
            'date_end': forms.SelectDateWidget(attrs={'class': 'form-calendar'}, years=range(1900, 2100)),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

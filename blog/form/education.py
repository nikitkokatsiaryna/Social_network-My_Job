from django import forms
from ..models import Education


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Education
        # fields = {'institution', 'user'}
        fields = '__all__'
        exclude = ('user',)

from django import forms
from ..models import Certificate


class CertificateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ('user',)

        widgets = {
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'date_end': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }

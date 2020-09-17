from django import forms
from ..models import Certificate


class CertificateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ('user',)

        widgets = {
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-calendar'}),
            'date_end': forms.SelectDateWidget(attrs={'class': 'form-calendar'}),
            'checkbox': forms.CheckboxInput(
                attrs={'class': 'checkbox', 'label': 'This certificate is perpetual'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

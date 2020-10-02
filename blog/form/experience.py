from django import forms
from ..models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ('user', 'checkbox')
        employment_choices = (
            ('FD', 'Full work day'),
            ('PE', 'Partial employment'),
            ('BM', 'Businessman'),
            ('F', 'Freelance'),
            ('C', 'Contract'),
            ('I', 'Internship'),
        )

        widgets = {
            'type_employment': forms.Select(choices=employment_choices,
                                            attrs={'class': 'form-control'}),
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-calendar'}, years=range(1900, 2100)),
            'date_end': forms.SelectDateWidget(attrs={'class': 'form-calendar'}, years=range(1900, 2100)),
            'checkbox': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

        labels = {
            'position': 'Position',
            'type_employment': 'Type employment',
            'company': 'Company',
            'region': 'Region',
            'checkbox': "I'm currently working in this position",
            'date_start': 'Date start',
            'date_end': 'Date end',
            'description': 'Description',
        }

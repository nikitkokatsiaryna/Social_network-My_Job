from django import forms
from ..models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        # fields = {"position"}
        fields = '__all__'
        exclude = ('user',)
        employment_choices = (
            ('FD', 'Full work day'),
            ('PE', 'Partial employment'),
            ('BM', 'Businessman'),
            ('F', 'Freelance'),
            ('C', 'Contract'),
            ('I', 'Internship'),
        )

        widgets = {
            'type_employment': forms.Select(choices=employment_choices, attrs={'class': 'form-control'}),
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-calendar'}),
            'date_end': forms.SelectDateWidget(attrs={'class': 'form-calendar'}),
            'checkbox': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
            # 'user': forms.HiddenInput()
        }

    labels = {
        'position': 'Position',
        'type_employment': 'Type employment',
        'company': 'Company',
        'region': 'Region',
        'checkbox': "I'm currently working in this position",
        'date_start': 'Date starttt',
        'date_end': 'Date end',
        'description': 'Description',
    }

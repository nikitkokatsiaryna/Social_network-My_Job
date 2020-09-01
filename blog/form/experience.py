from django import forms
from ..models import Experience


class ExperienceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Experience
        # fields = {"position"}
        fields = '__all__'
        exclude = ('user',)
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
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-group'}),
            'date_end': forms.SelectDateWidget(attrs={'class': 'form-group mx-sm-3 mb-2'}),
            # 'user': forms.HiddenInput()
        }

        labels = {
            'position': 'Position',
            'type_employment': 'Type employment',
            'company': 'Company',
            'region': 'Region',
            'date_start': 'Date start',
            'date_end': 'Date end',
            'description': 'Description',
        }
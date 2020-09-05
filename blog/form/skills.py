from django import forms
from ..models import Skill


class SkillForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Skill
        fields = ('name',)

        name = forms.CharField(label='search',
                            widget=forms.TextInput(attrs={'placeholder': 'Search'}))

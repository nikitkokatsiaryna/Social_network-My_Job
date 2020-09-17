from django import forms
from ..models import Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'profile_image':
                self.fields[field].widget.attrs['class'] = ''
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)

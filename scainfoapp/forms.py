from django import forms
from cafemapapp.models import Studycafes

class LikeForm(forms.ModelForm):
    class Meta:
        model=Studycafes
        fields=('sca_like',)
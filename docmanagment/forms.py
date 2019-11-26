from django import forms
from .models import Documnet,Category

class DocumnetModelForm(forms.ModelForm):
    class Meta:
        model=Documnet
        fields='__all__'
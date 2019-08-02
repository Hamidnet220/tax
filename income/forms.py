from django import forms
from .models import Income,Employeer

class AddEmployeerForm(forms.ModelForm):
    class Meta:
        model=Employeer
        fields='__all__'

    def save_record(self):
        Employeer.objects.create(**self.cleaned_data)

class AddIncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields='__all__'
        

    def save_record(self):
        Income.objects.create(**self.cleaned_data)
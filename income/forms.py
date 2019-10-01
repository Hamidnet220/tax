from django import forms
from .models import Income,Employeer

class AddEmployeerForm(forms.ModelForm):
    class Meta:
        model=Employeer
        fields='__all__'

    def save_record(self):
        Employeer.objects.create(**self.cleaned_data)

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields='__all__'
        
    def save_record(self):
        Income.objects.create(**self.cleaned_data)

    def update_record(self,id):
        Income.objects.filter(id=id).update(**self.cleaned_data)

class SeasonReport(forms.Form):
    seasons=[(1,'بهار'),(2,'تابستان'),(3,'‍پاییز'),(4,'زمستان')]
    season=forms.ChoiceField(choices=seasons)
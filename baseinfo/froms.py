from django import forms
from .models import *


# Employer create form
class AddEmployerForm(forms.ModelForm):
    class Meta:
        model=Employer
        fields='__all__'

    def save_record(self):
        Employer.objects.create(**self.cleaned_data)

# Contract create form
class AddContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields='__all__'

    def save_record(self):
        Contract.objects.create(**self.cleaned_data)

# Create bank form
class BankForm(forms.ModelForm):
    class Meta:
        model=Bank
        fields='__all__'
    
    def save_record(self):
        Bank.objects.create(**self.cleaned_data)
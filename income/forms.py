from django import forms
from .models import Income, Employeer, Bank, Contract, Buy

class AddEmployeerForm(forms.ModelForm):
    class Meta:
        model=Employeer
        fields='__all__'

    def save_record(self):
        Employeer.objects.create(**self.cleaned_data)

class AddContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields='__all__'

    def save_record(self):
        Contract.objects.create(**self.cleaned_data)

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields='__all__'
        
    def save_record(self):
        Income.objects.create(**self.cleaned_data)

    def update_record(self,id):
        Income.objects.filter(id=id).update(**self.cleaned_data)

class BuyForm(forms.ModelForm):
    class Meta:
        model=Buy
        fields='__all__'
        
    def save_record(self):
        Buy.objects.create(**self.cleaned_data)

    def update_record(self,id):
        Buy.objects.filter(id=id).update(**self.cleaned_data)

class SeasonReport(forms.Form):
    seasons=[(1,'بهار'),(2,'تابستان'),(3,'‍پاییز'),(4,'زمستان')]
    season=forms.ChoiceField(choices=seasons,widget=forms.Select(attrs={'onchange':'this.form.submit();'}))
    file_path=forms.FileField(allow_empty_file=True)

class EmployerPyementReport(forms.Form):
    field=Employeer.objects.all()
    employer=forms.ModelChoiceField(queryset=field,widget=forms.Select(attrs={'onchange':'this.form.submit();'}))

class ContractPymentReport(forms.Form):
    field=Contract.objects.all()
    contract=forms.ModelChoiceField(queryset=field,widget=forms.Select(attrs={'onchange':'this.form.submit();'}))
     

class BankForm(forms.ModelForm):
    class Meta:
        model=Bank
        fields='__all__'
    
    def save_record(self):
        Bank.objects.create(**self.cleaned_data)
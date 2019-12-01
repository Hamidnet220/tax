from django.shortcuts import render
from django.urls import reverse_lazy
from views_generator import ViewGenerator
from django.db.models import Sum
from income.models import Income
from django.views.generic import FormView
from .froms import *
from .models import *

# Contract list view
def get_contracts_list_view(request,*args,**kwargs):
    
   contracts=Contract.objects.all()
   for contract in contracts:
       contract_amount=contract.gross_amount + contract.adjustment_amount
       incomes=Income.objects.filter(contract=contract)
       total_income=incomes.aggregate(Sum('gross_amount'))
       contract.total_payments=total_income['gross_amount__sum']
       contract.final_amount=contract_amount
       if contract.total_payments is not None:
        contract.progress='{0:.3g}'.format(total_income['gross_amount__sum']/contract_amount)
       else:
        contract.total_payments=0
        contract.progress=0

       contract.save()
    

   view=ViewGenerator(table=Contract,
                     opration_buttons={},select_checkbox=False,add_url='baseinfo:contract-create')
   return render(request,"baseinfo/contracts_list.html",view.get_context_template())  

# Create contract view
class AddContractView(FormView):
    template_name   =   'share/input_form.html'
    form_class      =   AddContractForm
    success_url     =   reverse_lazy('contract-list')
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

# Employers list view
def get_employers_list_view(request,*args,**kwargs):
    view=ViewGenerator(table=Employer,opration_buttons={},select_checkbox=False,
                        add_url='baseinfo:employer-create')
    return render(request,"baseinfo/employer_list.html",view.get_context_template())

# Create employer view
class AddEmployerView(FormView):
    template_name   =   'share/input_form.html'
    form_class      =   AddEmployerForm
    success_url     =   reverse_lazy('employers')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

# Update employer view
def update_employer_view(request,id):
    if request.method=='POST':
        employer=Employer.objects.get(id=id)
        form=AddEmployerForm(employer)


# Bank list view
def get_banks(request,*args,**kwargs):
    
    view=ViewGenerator(table=Bank,opration_buttons={},
                        select_checkbox=False,add_url='baseinfo:bank-create')

    return render(request,"share/list.html",view.get_context_template())

# Create bank view
class AddBankView(FormView):
    template_name   =   'share/input_form.html'
    form_class      =   BankForm
    success_url     =   reverse_lazy('baseinfo:bank-list')
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

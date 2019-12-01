from django.shortcuts import render
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView
from .models import Income,Contract
from .forms import *
from views_generator import ViewGenerator
from django.forms import modelformset_factory
import decimal


# Incomes view
def get_incomes_view(request,*args,**kwargs):
    ordering=('year','month','day')
    for income in Income.objects.all():
        income.tax_amount=round(income.gross_amount * decimal.Decimal(0.03),0)
        if income.VAT_included == True:
            income.VAT_amount =round(income.gross_amount*decimal.Decimal(0.09),0)
        income.save()
        
    view=ViewGenerator(table=Income,opration_buttons={},
                        select_checkbox=False,add_url='income:income-create',ordering=ordering)

    return render(request,"share/list.html",view.get_context_template())

# Add new income view
class AddIncomeView(FormView):
    template_name   =   'share/input_form.html'
    form_class      =   IncomeForm
    success_url     =   reverse_lazy('income-list')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

# Buys view 
def get_buys_view(request,*args,**kwargs):
    ordering=('year','month','day')
    view=ViewGenerator(table=Buy,opration_buttons={},
                        select_checkbox=False,add_url='income:buy-create',ordering=ordering)

    return render(request,"share/list.html",view.get_context_template())

# Add new buy view
class AddBuyView(FormView):
    template_name   =   'share/input_form.html'
    form_class      =   BuyForm
    success_url     =   reverse_lazy('buy-list')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

#Session Report view
def get_season_view(request,*args,**kwargs):

    if request.method=='POST':
        if request.POST['season']=='1':
            incoms=Income.objects.filter(month__in=[1,2,3]).filter(year=1398)
        elif request.POST['season']=='2':
            incoms=Income.objects.filter(month__in=[4,5,6]).filter(year=1398)
        elif request.POST['season']=='3':
            incoms=Income.objects.filter(month__in=[7,8,9]).filter(year=1398)
        elif request.POST['season']=='4':
            incoms=Income.objects.filter(month__in=[10,11,12]).filter(year=1398)
            
        ordering=('year','month','day')
        form=SeasonReport(request.POST)

        view=ViewGenerator(table=Income,entities=incoms,opration_buttons={},
                    select_checkbox=False,add_url='income-create',ordering=ordering)
        total_income=incoms.aggregate(Sum('gross_amount'))
        total_tax=incoms.aggregate(Sum('tax_amount'))
        total_VAT=incoms.aggregate(Sum('VAT_amount'))
        total_pay=incoms.aggregate(Sum('pay_amount'))
        total_fields={'total_income':total_income,'total_tax':total_tax,
        'total_VAT':total_VAT,'total_pay':total_pay}
        context=view.get_context_template()
        additon={'form':form}
        exclude_fields={'exclude':['description']}
        context.update(**additon)
        context.update(**total_fields)
        context.update(**exclude_fields)
        print(total_fields)
        return render(request,"income/season_report.html",context)
    else:    
        form=SeasonReport()
        return render(request,"income/season_report.html",{'form':form})

#Get all incoms in specfic year as declarations
def declaration_view(request,*args,**kwargs):
    incomes=Income.objects.filter(year=1398)

    

    ordering=('year','month','day')
    view=ViewGenerator(table=Income,entities=incomes,opration_buttons={},select_checkbox=False,
    add_url='',ordering=ordering)

    #Total fields 
    total_income=incomes.aggregate(Sum('gross_amount'))
    total_tax=incomes.aggregate(Sum('tax_amount'))
    total_VAT=incomes.aggregate(Sum('VAT_amount'))
    total_pay=incomes.aggregate(Sum('pay_amount'))
    total_fields={'total_income':total_income,'total_tax':total_tax,
        'total_VAT':total_VAT,'total_pay':total_pay}

    #Exclude fields
    exclude_fields={'exclude':['بانک','description','bank']}
    
    #crate context for template
    context=view.get_context_template()

    # add total fields to context
    context.update(**total_fields)

    #add exclude fields to context 
    context.update(**exclude_fields)

     
    return render(request,"income/declaration.html",context)
    


def get_employer_payment_view(request,*args,**kwargs):
    if request.method=='POST':
        ordering=('year','month','day')
        form=EmployerPyementReport(request.POST)
        empolyer=int(request.POST['employer'])
        incoms=Income.objects.filter(employer_id=empolyer)
        total_income=Income.objects.filter(employer_id=empolyer).aggregate(Sum('gross_amount'))
        total_tax=Income.objects.filter(employer_id=empolyer).aggregate(Sum('tax_amount'))
        total_VAT=Income.objects.filter(employer_id=empolyer).aggregate(Sum('VAT_amount'))
        total_pay=Income.objects.filter(employer_id=empolyer).aggregate(Sum('pay_amount'))
        view=ViewGenerator(table=Income,entities=incoms,opration_buttons={},
                    select_checkbox=False,add_url='add_income',ordering=ordering)
        context=view.get_context_template()
        additon={'form':form}
        total_fields={'total_income':total_income,'total_tax':total_tax,
        'total_VAT':total_VAT,'total_pay':total_pay}
        exclude_fields={'exclude':['description']}
        context.update(**additon)
        context.update(**total_fields)
        context.update(**exclude_fields)
        print(context)
        return render(request,"income/employer_payment_list.html",context)
    else:
        form=EmployerPyementReport()
    
    return render(request,"income/employer_payment_list.html",{'form':form})

def get_contracts_view(request,id,*args,**kwargs):
   contracts=Contract.objects.filter(employer_id=id)
   for contract in contracts:
       contract_amount=contract.gross_amount
       incomes=Income.objects.filter(contract=contract)
       total_income=incomes.aggregate(Sum('gross_amount'))
       contract.final_amount=total_income['gross_amount__sum']
       contract.progress='{0:.3g}'.format(total_income['gross_amount__sum']/contract_amount)
       contract.save()
    

   view=ViewGenerator(table=Contract,entities=contracts,
                     opration_buttons={},select_checkbox=False,add_url='employer-create')
   print(view.get_context_template())
   return render(request,"share/list.html",view.get_context_template())  

    
def get_contract_payments_view(request,*args,**kwargs):
    if request.method=='POST':
        ordering=('year','month','day')
        form=ContractPymentReport(request.POST)
        contract=int(request.POST['contract'])
        incoms=Income.objects.filter(contract_id=contract)
        total_income=Income.objects.filter(contract_id=contract).aggregate(Sum('gross_amount'))
        total_tax=Income.objects.filter(contract_id=contract).aggregate(Sum('tax_amount'))
        total_VAT=Income.objects.filter(contract_id=contract).aggregate(Sum('VAT_amount'))
        total_pay=Income.objects.filter(contract_id=contract).aggregate(Sum('pay_amount'))
        view=ViewGenerator(table=Income,entities=incoms,opration_buttons={},
                    select_checkbox=False,add_url='income-create',ordering=ordering)
        context=view.get_context_template()
        additon={'form':form}
        total_fields={'total_income':total_income,'total_tax':total_tax,
        'total_VAT':total_VAT,'total_pay':total_pay}
        exclude_fields={'exclude':['description']}
        context.update(**additon)
        context.update(**total_fields)
        context.update(**exclude_fields)
        return render(request,"income/contract_payment_list.html",context)
    else:
        form=ContractPymentReport()
    
    return render(request,"income/contract_payment_list.html",{'form':form})


from django.shortcuts import render
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView
from .models import Income
from .forms import *
from views_generator import ViewGenerator
# Create your views here.

class home_view(TemplateView):
    template_name="home.html"

# Incomes view
def get_incomes_view(request,*args,**kwargs):
    ordering=('year','month','day')
    view=ViewGenerator(table=Income,opration_buttons={},
                        select_checkbox=False,add_url='add_income',ordering=ordering)

    return render(request,"list_objects.html",view.get_context_template())

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
                    select_checkbox=False,add_url='add_income',ordering=ordering)
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
        return render(request,"season_report.html",context)
    else:    
        form=SeasonReport()
        return render(request,"season_report.html",{'form':form})

# Employeers view
def get_employeers_view(request,*args,**kwargs):
    view=ViewGenerator(table=Employeer,opration_buttons={},select_checkbox=False,
                        add_url='add_employeer')
    return render(request,"list_objects.html",view.get_context_template())

class AddEmployeerView(FormView):
    template_name   =   'input_form.html'
    form_class      =   AddEmployeerForm
    success_url     =   reverse_lazy('employeers')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddIncomeView(FormView):
    template_name   =   'input_form.html'
    form_class      =   IncomeForm
    success_url     =   reverse_lazy('incomes')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def get_employer_payment_view(request,*args,**kwargs):
    if request.method=='POST':
        ordering=('year','month','day')
        form=EmployerPyementReport(request.POST)
        print(request.POST)
        empolyer=int(request.POST['employer'])
        incoms=Income.objects.filter(employeer_id=empolyer)
        total_income=Income.objects.filter(employeer_id=empolyer).aggregate(Sum('gross_amount'))
        total_tax=Income.objects.filter(employeer_id=empolyer).aggregate(Sum('tax_amount'))
        total_VAT=Income.objects.filter(employeer_id=empolyer).aggregate(Sum('VAT_amount'))
        total_pay=Income.objects.filter(employeer_id=empolyer).aggregate(Sum('pay_amount'))
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
        return render(request,"employer_payment_list.html",context)
    else:
        form=EmployerPyementReport()
    
    return render(request,"employer_payment_list.html",{'form':form})



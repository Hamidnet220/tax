from django.shortcuts import render
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
    view=ViewGenerator(Income,{},False,'add_income',ordering)
    return render(request,"list_objects.html",view.get_context_template())

# Employeers view
def get_employeers_view(request,*args,**kwargs):
    view=ViewGenerator(Employeer,{},False,'add_employeer')
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

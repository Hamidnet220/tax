from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Income
from views_generator import ViewGenerator
# Create your views here.

class home_view(TemplateView):
    template_name="home.html"

# Incomes view
def get_incomes_view(request,*args,**kwargs):
    view=ViewGenerator(Income,{},False,'add_income')
    return render(request,"list_objects.html",view.get_context_template())
def add_income_view(requset,*args,**kwargs):
    pass


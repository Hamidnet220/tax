"""tax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from income.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view.as_view(),name='home'),
    path('employeers/',get_employeers_view,name="employeers"),
    path('employeers/add',AddEmployeerView.as_view(),name="add_employeer"),
    path('incomes/',get_incomes_view,name='incomes'),
    path('incomes/add/',AddIncomeView.as_view(),name='add_income'),
    path('banks/',get_banks,name="banks"),
    path('banks/add',AddBankView.as_view(),name="add_bank")

]

urlpatterns+=[
    path('report/',include('income.urls'))
]



from django.urls import path
from .views import *

app_name = 'income'

urlpatterns=[
    path("",get_incomes_view, name = "income-list"),
    path("create/", AddIncomeView.as_view(), name = "income-create"),
    path("buys/",get_buys_view, name = "buy-list"),
    path("buy/create/", AddBuyView.as_view(),name="buy-create"),
    path("season-report/",get_season_view,name="season-report"),
    path("employer-pays/",get_employer_payment_view,name="employer-pays"),
    path("contract-pays/",get_contract_payments_view,name="contract-pays"),
    path("declaration/",declaration_view,name="declaration"),
    path('employer-contracts/<int:id>',get_contracts_view,name="employer-contracts"),
]

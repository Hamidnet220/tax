
from django.urls import path
from .views import *
urlpatterns=[
    path("season_report/",get_season_view,name="season_report"),
    path("employer_payment/",get_employer_payment_view,name="employer_payment"),
    path("contract_payments/",get_contract_payments_view,name="contract_payments"),
    path("declaration/",declaration_view,name="declaration"),
    path('employer/contracts/<int:id>',get_contracts_view,name='contracts'),
]
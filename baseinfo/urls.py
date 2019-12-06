from django.urls import path
from .views import (get_contracts_list_view,
                    AddContractView,
                    get_employers_list_view,
                    AddEmployerView,
                    get_banks,
                    AddBankView,
                    CompanyInfo_View)
app_name = 'baseinfo'
urlpatterns=[
    path("contracts/", get_contracts_list_view, name = "contract-list"),
    path("contract/create/", AddContractView.as_view(), name = "contract-create"),
    path('employers/', get_employers_list_view, name = "employer-list"),
    path("employer/create/", AddEmployerView.as_view(), name = "employer-create"),
    path("banks/", get_banks, name = "bank-list"),
    path("bank/create/",AddBankView.as_view(), name = "bank-create" ),
    path("companyInfo",CompanyInfo_View.as_view(),name = "companyInfo-list"),
]
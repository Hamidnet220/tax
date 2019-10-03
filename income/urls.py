
from django.urls import path
from .views import *
urlpatterns=[
    path("season_report/",get_season_view,name="season_report"),
    path("employer_payment/",get_employer_payment_view,name="employer_payment")
]
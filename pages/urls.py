from django.urls import path
from django.contrib.auth import views as Auth_Views
from .views import *

app_name='pages'

urlpatterns=[
    path('',home,name='home'),
    path('login/',Auth_Views.LoginView.as_view(template_name='pages/login.html')),
    path('logout/',Auth_Views.LogoutView.as_view(template_name='pages/home.html')),
]


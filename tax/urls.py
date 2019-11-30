from django.contrib import admin
from django.urls import path,include
from income.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('documents/',include('docmanagment.urls')),
    path('baseinfo/',include('baseinfo.urls')),
    path('income/',include('income.urls')),
    ]
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import static
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc', include('django.contrib.admindocs.urls')),
    path('',include('pages.urls')),
    path('documents/',include('docmanagment.urls')),
    path('baseinfo/',include('baseinfo.urls')),
    path('income/',include('income.urls')),
    ]
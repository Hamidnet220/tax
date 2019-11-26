from django.urls import path
from .views import *

urlpatterns=[
    path('',DocumentListView.as_view(),name='document-list'),
    path('detail/<int:pk>/',DocumentDetailView.as_view(),name='document-detail'),
    path('create/',DocumentCreateView.as_view(),name='document-create'),

]
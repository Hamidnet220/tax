from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse 
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView   
from views_generator import ViewGenerator
from .forms import *
from .models import *
import datetime
import os
# Create your views here.


class DocumentListView(ListView):
    
    template_name = 'document_list.html'
    queryset = Documnet.objects.all()

class DocumentDetailView(DetailView):
    template_name = 'document_detail.html'
    queryset = Documnet.objects.all()

class DocumentCreateView(CreateView):
    template_name = 'upload_doc.html'
    form_class = DocumnetModelForm
    queryset = Documnet.objects.all() 

    def form_valid(self,form):
        form.instance.added_by_user = self.request.user
        return super().form_valid(form)

class DocDelete(DeleteView):
    model=Documnet
    success_url=reverse_lazy('doc-list')

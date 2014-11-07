from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView

# Create your views here.
class CategoryView(TemplateView):
    #code
    template_name='categos/cat.html'


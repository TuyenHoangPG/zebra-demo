from django.shortcuts import render
from django.views.generic import FormView, TemplateView


# Create your views here.
class SuccessView(TemplateView):
    template_name = "list-task.html"

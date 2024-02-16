from django.shortcuts import render
from django.views.generic import FormView, TemplateView


# Create your views here.
class ListTaskView(TemplateView):
    template_name = "task/list-task.html"

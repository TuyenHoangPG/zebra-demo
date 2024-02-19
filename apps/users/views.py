from django.shortcuts import render
from django.views.generic import FormView, TemplateView


# Create your views here.
class ListUserView(TemplateView):
    template_name = "users/list-user.html"

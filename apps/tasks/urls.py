from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.ListTaskView.as_view(), name="list_task"),
]

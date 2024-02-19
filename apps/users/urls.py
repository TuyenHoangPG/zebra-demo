from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.ListUserView.as_view(), name="list-user"),
]

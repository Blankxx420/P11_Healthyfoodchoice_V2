from django.urls import path

from . import views

app_name = "autocomplete"

urlpatterns = [path("", views.complete, name="complete")]
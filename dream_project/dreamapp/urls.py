from . import views
from django.urls import path

urlpatterns = [
    path('', views.display_form, name="display_form"),
    path("result", views.display_result, name="display_result")
]
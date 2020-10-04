from django.urls import path
from . import views

urlpatterns = [
    path('', views.OcorrenciasListCreate.as_view()),
]
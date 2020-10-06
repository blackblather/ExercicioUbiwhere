from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('', views.OcorrenciasListCreate.as_view()),
    path('autor/<int:autor>/', views.OcorrenciasListCreate.as_view()),
    path('categoria/<int:categoria>/', views.OcorrenciasListCreate.as_view()),
    path('autor/<int:autor>/categoria/<int:categoria>/', views.OcorrenciasListCreate.as_view()),
    path('validate-ocorrencia/', views.OcorrenciasUpdate.as_view()),
    path('api-token-auth/', auth_views.obtain_auth_token)
]
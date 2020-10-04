from .models import Ocorrencias
from .serializers import OcorrenciasSerializer
from rest_framework import generics


class OcorrenciasListCreate(generics.ListCreateAPIView):
    queryset = Ocorrencias.objects.all()
    serializer_class = OcorrenciasSerializer
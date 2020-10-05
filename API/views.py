from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import OcorrenciasSerializer
from rest_framework import generics, status
from .models import Ocorrencias


class OcorrenciasListCreate(generics.ListCreateAPIView):
    queryset = Ocorrencias.objects.all()
    serializer_class = OcorrenciasSerializer


class OcorrenciasUpdate(generics.UpdateAPIView):
    queryset = Ocorrencias.objects.all()
    serializer_class = OcorrenciasSerializer

    permission_classes = [IsAdminUser]

    def __validate_request_format(self, request):
        if not (request.data.__len__() == 1 and 'id' in request.data.keys()):
            raise ValueError("Malformed request format. Expected JSON object with key 'id'.")

    def partial_update(self, request, *args, **kwargs):
        try:
            self.__validate_request_format(request)
            ocorrencia = get_object_or_404(self.queryset, pk=request.data["id"])
            serializer = self.serializer_class(ocorrencia, data={"estado": 2}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as error:
            return Response(error.__str__(), status=status.HTTP_400_BAD_REQUEST)

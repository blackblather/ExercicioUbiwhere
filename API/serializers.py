from rest_framework import serializers
from .models import Ocorrencias


class OcorrenciasSerializer(serializers.ModelSerializer):
    data_criacao = serializers.DateField()
    data_atualizacao = serializers.DateField(required=False)

    class Meta:
        model = Ocorrencias
        fields = ['id', 'descricao', 'lat', 'lon', 'data_criacao', 'data_atualizacao', 'autor', 'estado', 'categoria']

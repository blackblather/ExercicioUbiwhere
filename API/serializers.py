from rest_framework import serializers
from .models import Ocorrencias


class OcorrenciasSerializer(serializers.ModelSerializer):
    autor = serializers.ReadOnlyField(source="autor.username")
    estado = serializers.ReadOnlyField(source="estado.estado")
    categoria = serializers.ReadOnlyField(source="categoria.categoria")
    data_criacao = serializers.DateField()
    data_atualizacao = serializers.DateField()

    class Meta:
        model = Ocorrencias
        fields = ['id', 'descricao', 'lat', 'lon', 'data_criacao', 'data_atualizacao', 'autor', 'estado', 'categoria']

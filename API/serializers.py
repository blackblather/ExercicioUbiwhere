from rest_framework import serializers
from .models import Ocorrencias


class OcorrenciasSerializer(serializers.ModelSerializer):
    data_criacao = serializers.DateField()
    data_atualizacao = serializers.DateField(required=False)

    def create(self, validated_data):
        if 'estado' in validated_data.keys():
            validated_data.pop('estado')
        return Ocorrencias.objects.create(**validated_data)

    class Meta:
        model = Ocorrencias
        fields = ['id', 'descricao', 'lat', 'lon', 'data_criacao', 'data_atualizacao', 'autor', 'estado', 'categoria']

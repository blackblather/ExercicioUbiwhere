from django.db import models
from django.contrib.auth.models import User


class Estados(models.Model):
    estado = models.CharField(max_length=256)


class Categorias(models.Model):
    categoria = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256)


class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=256)
    lat = models.FloatField()
    lon = models.FloatField()
    data_criacao = models.DateField()
    data_atualizacao = models.DateField()

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.ForeignKey('Estados', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE)

# Generated by Django 3.1.2 on 2020-10-07 00:27

from django.db import migrations, models


def __populate_estados(apps):
    Estados = apps.get_model('API', 'Estados')
    e = Estados(estado="Por validar")
    e.save()
    e = Estados(estado="Validado")
    e.save()
    e = Estados(estado="Resolvido")
    e.save()


def __populate_categorias(apps):
    Categorias = apps.get_model('API', 'Categorias')
    c = Categorias(categoria="CONSTRUCTION", descricao="Eventos planeados de obras nas estradas")
    c.save()
    c = Categorias(categoria="SPECIAL_EVENT", descricao="Eventos especiais (concertos, feiras, etc)")
    c.save()
    c = Categorias(categoria="INCIDENT", descricao="Acidentes ou outros eventos inesperados")
    c.save()
    c = Categorias(categoria="WEATHER_CONDITION", descricao="Eventos meteorológicos que afetam as estradas")
    c.save()
    c = Categorias(categoria="ROAD_CONDITION", descricao="Estados das estradas que afetem quem circula nestas (piso degradado, buracos, etc)")
    c.save()


def populate_dataset(apps, schema_editor):
    __populate_estados(apps)
    __populate_categorias(apps)


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20201004_1022'),
    ]

    operations = [
        migrations.RunPython(populate_dataset),
    ]
# Generated by Django 5.1.4 on 2024-12-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_anime_remove_pelicula_categorias_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='episodes',
            field=models.CharField(max_length=255),
        ),
    ]
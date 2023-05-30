# Generated by Django 4.0.10 on 2023-05-29 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0004_cliente_oficina_cliente_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='data_encerramento',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_incio',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cliente',
            name='valor_pecas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cliente',
            name='valor_servico',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='servico',
            field=models.CharField(default="", max_length=300),
        ),
    ]

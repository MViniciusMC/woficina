# Generated by Django 4.0.10 on 2023-05-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0008_alter_login_chave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='valor_pecas',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='valor_servico',
            field=models.FloatField(default=0),
        ),
    ]

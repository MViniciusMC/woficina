# Generated by Django 4.0.10 on 2023-05-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0006_alter_cliente_data_encerramento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='chave',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='login',
            name='oficina',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='senha',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='login',
            name='usuario',
            field=models.CharField(default='', max_length=100),
        ),
    ]

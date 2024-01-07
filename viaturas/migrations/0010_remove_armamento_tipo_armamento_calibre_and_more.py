# Generated by Django 4.2.1 on 2024-01-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0009_alter_consumomun_quantidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armamento',
            name='tipo',
        ),
        migrations.AddField(
            model_name='armamento',
            name='calibre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='armamento',
            name='fabricante',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='armamento',
            name='modelo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='armamento',
            name='classificacao',
            field=models.CharField(choices=[('Fuzil 7,62mm', 'Fuzil 7,62mm'), ('Pistola 9mm', 'Pistola 9mm'), ('Metralhadora MAG', 'Metralhadora MAG'), ('FAP', 'FAP'), ('FAC', 'FAC'), ('Metralhadora .50', 'Metralhadora .50'), ('Fuzil 5,56mm', 'Fuzil 5,56mm'), ('Espingarda 12', 'Espingarda 12'), ('Morteiro Pesado 120mm', 'Morteiro Pesado 120mm'), ('Obuseiro 105mm', 'Obuseiro 105mm'), ('Obuseiro 155mm', 'Obuseiro 155mm'), ('Faca', 'Faca'), ('Outros', 'Outros')], default='Outros', max_length=50),
        ),
    ]
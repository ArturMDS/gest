# Generated by Django 4.2.1 on 2023-11-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0004_viatura_odometro_viatura_placa_municao_armamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='armamento',
            name='classificacao',
            field=models.CharField(choices=[('Fuzil 7,62mm', 'Fuzil 7,62mm'), ('Pistola 9mm', 'Pistola 9mm'), ('Metrlhadora MAG', 'Metrlhadora MAG'), ('FAP', 'FAP'), ('FAC', 'FAC'), ('Metrlhadora .50', 'Metrlhadora .50'), ('Fuzil 5,56mm', 'Fuzil 5,56mm'), ('Espingarda 12', 'Espingarda 12'), ('Morteiro Pesado 120mm', 'Morteiro Pesado 120mm'), ('Obuseiro 105mm', 'Obuseiro 105mm'), ('Obuseiro 155mm', 'Obuseiro 155mm'), ('Faca', 'Faca'), ('Outros', 'Outros')], default='Outros', max_length=50),
        ),
        migrations.AddField(
            model_name='municao',
            name='classificacao',
            field=models.CharField(choices=[('Mun 7,62mm Comum', 'Mun 7,62mm Comum'), ('Mun 9mm', 'Mun 9mm'), ('Mun 7,62mm Tr', 'Mun 7,62mm Tr'), ('Mun .50', 'Mun .50'), ('Mun 5,56mm', 'Mun 5,56mm'), ('Mun Cal 12', 'Mun Cal 12'), ('Mun menos letal', 'Mun menos letal'), ('Gr menos letal', 'Gr menos letal'), ('Mun 120mm', 'Mun 120mm'), ('Mun 105mm', 'Mun 105mm'), ('Mun 155mm', 'Mun 155mm'), ('Outros', 'Outros')], default='Outros', max_length=50),
        ),
    ]

# Generated by Django 4.2.1 on 2024-01-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaturas', '0012_alter_alteracao_data_alter_consumomun_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamento',
            name='outros_nr_serie',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-11-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('militares', '0019_alter_atributos_ranking_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='militar',
            name='identidade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

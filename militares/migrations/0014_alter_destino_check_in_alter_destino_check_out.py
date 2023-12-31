# Generated by Django 4.2.1 on 2023-10-16 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('militares', '0013_destino_in_force'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='check_in',
            field=models.DateTimeField(help_text='dd/mm/aaaa hh:mm:ss'),
        ),
        migrations.AlterField(
            model_name='destino',
            name='check_out',
            field=models.DateTimeField(blank=True, help_text='dd/mm/aaaa hh:mm:ss', null=True),
        ),
    ]

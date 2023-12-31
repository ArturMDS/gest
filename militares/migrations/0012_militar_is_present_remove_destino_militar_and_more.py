# Generated by Django 4.2.1 on 2023-10-15 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('militares', '0011_destino'),
    ]

    operations = [
        migrations.AddField(
            model_name='militar',
            name='is_present',
            field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(
            model_name='destino',
            name='militar',
        ),
        migrations.AddField(
            model_name='destino',
            name='militar',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='destino', to='militares.militar'),
            preserve_default=False,
        ),
    ]

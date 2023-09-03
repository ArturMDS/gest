# Generated by Django 4.2.1 on 2023-07-09 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subunidades', '0001_initial'),
        ('militares', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='militar',
            name='subunidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mil_su', to='subunidades.subunidade'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-11-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subunidades', '0003_subunidade_abreviatura_subunidade_cmt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subunidade',
            name='abreviatura',
            field=models.CharField(default='Coloque a abreviatura', max_length=40),
        ),
    ]

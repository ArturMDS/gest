# Generated by Django 4.2.1 on 2023-12-04 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subunidades', '0007_alter_subunidade_acesso_encmat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subunidade',
            name='acesso_mil',
        ),
    ]

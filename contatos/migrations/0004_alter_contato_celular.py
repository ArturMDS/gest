# Generated by Django 4.2.1 on 2023-11-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_alter_contato_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='celular',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.2.1 on 2023-11-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_alter_documento_cat_cnh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='cat_cnh',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Categoria da CNH'),
        ),
    ]

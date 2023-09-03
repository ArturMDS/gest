# Generated by Django 4.2.1 on 2023-07-09 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0003_remove_documento_pessoa_remove_endereco_pessoa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('titulo_eleitor', models.CharField(max_length=50)),
                ('cnh', models.CharField(blank=True, max_length=20, null=True)),
                ('cat_cnh', models.CharField(blank=True, max_length=1, null=True)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='documento', to='pessoas.pessoa')),
            ],
        ),
    ]

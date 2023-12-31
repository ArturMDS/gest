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
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logadouro', models.CharField(max_length=200)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('bairro', models.CharField(max_length=80)),
                ('cep', models.CharField(max_length=9)),
                ('cidade', models.CharField(max_length=80)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='pessoas.pessoa')),
            ],
        ),
    ]

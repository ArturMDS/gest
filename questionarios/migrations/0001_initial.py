# Generated by Django 4.2.1 on 2023-10-31 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0007_alter_banco_pessoa_alter_pessoa_fator_rh_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=200)),
                ('pontos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gabarito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=100)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resposta', to='pessoas.pessoa')),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gabarito', to='questionarios.questao')),
            ],
        ),
    ]

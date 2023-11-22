# Generated by Django 4.2.1 on 2023-11-10 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_alter_banco_pessoa_alter_pessoa_fator_rh_and_more'),
        ('questionarios', '0007_alter_questionariodois_pessoa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatorioCS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obs_questionario', models.CharField(blank=True, max_length=400, null=True, verbose_name='Observações dos Questinários')),
                ('obs_entrevistador', models.TextField(blank=True, max_length=400, null=True, verbose_name='Observações do Entrevistador')),
                ('sugestao', models.CharField(choices=[('Sem Sugestão', 'Sem Sugestão'), ('Não deve Servir', 'Não deve Servir'), ('Pode Servir', 'Pode Servir'), ('Deve Servir', 'Deve Servir')], default='Sem Sugestão', max_length=50)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='relatorio_cs', to='pessoas.pessoa')),
            ],
        ),
    ]

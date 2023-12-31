# Generated by Django 4.2.1 on 2023-11-07 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_alter_banco_pessoa_alter_pessoa_fator_rh_and_more'),
        ('questionarios', '0005_questionarioum_pergunta_cinco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionariodois',
            name='pergunta_nove',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='questionariodois',
            name='pergunta_seis',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Questionariotres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta_um', models.CharField(max_length=3)),
                ('pergunta_dois', models.CharField(max_length=3)),
                ('pergunta_tres', models.CharField(max_length=300)),
                ('pergunta_quatro', models.CharField(max_length=3)),
                ('pergunta_cinco', models.CharField(max_length=3)),
                ('pergunta_seis', models.CharField(max_length=300)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questionario_tres', to='pessoas.pessoa')),
            ],
        ),
    ]

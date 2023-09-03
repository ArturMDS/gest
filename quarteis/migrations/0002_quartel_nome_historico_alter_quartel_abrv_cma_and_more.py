# Generated by Django 4.2.1 on 2023-07-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quarteis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quartel',
            name='nome_historico',
            field=models.CharField(blank=True, help_text='Nome por Extenso', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='quartel',
            name='abrv_cma',
            field=models.CharField(blank=True, help_text='Abreviatura do Cmdo Mil A', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='quartel',
            name='abrv_divisao',
            field=models.CharField(blank=True, help_text='Abreviatura da Divisão de Exército', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='quartel',
            name='abrv_esc_sup',
            field=models.CharField(blank=True, help_text='Abreviatura do Esc Sup', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='quartel',
            name='cmdo_mil_a',
            field=models.CharField(blank=True, help_text='Nome por Extenso', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='quartel',
            name='divisao',
            field=models.CharField(blank=True, help_text='Nome por Extenso', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='quartel',
            name='esc_sup',
            field=models.CharField(blank=True, help_text='Nome por Extenso', max_length=70, null=True),
        ),
    ]

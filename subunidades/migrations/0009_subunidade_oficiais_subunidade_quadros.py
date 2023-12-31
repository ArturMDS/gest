# Generated by Django 4.2.1 on 2023-12-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0008_alter_pessoa_nome_mae'),
        ('subunidades', '0008_remove_subunidade_acesso_mil'),
    ]

    operations = [
        migrations.AddField(
            model_name='subunidade',
            name='oficiais',
            field=models.ManyToManyField(blank=True, related_name='su_oficiais', to='pessoas.pessoa'),
        ),
        migrations.AddField(
            model_name='subunidade',
            name='quadros',
            field=models.ManyToManyField(blank=True, related_name='su_quadros', to='pessoas.pessoa'),
        ),
    ]

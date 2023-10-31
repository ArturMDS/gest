# Generated by Django 4.2.1 on 2023-10-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_pessoa_fator_rh_pessoa_peso_pessoa_tipo_sanguineo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='altura',
            field=models.DecimalField(decimal_places=2, default=1.7, max_digits=3),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='escolaridade',
            field=models.CharField(choices=[('Fundamental Incompleto', 'Fundamental Incompleto'), ('Fundamental Completo', 'Fundamental Completo'), ('Médio Incompleto', 'Médio Incompleto'), ('Médio Completo', 'Médio Completo'), ('Superior Incompleto', 'Superior Incompleto'), ('Superior Completo', 'Superior Completo'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], default='Fundamental Incompleto', max_length=60),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='religiao',
            field=models.CharField(default='Não declarado', max_length=100),
        ),
    ]
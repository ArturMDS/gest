# Generated by Django 4.2.1 on 2023-11-20 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subunidades', '0006_subunidade_acesso_encmat_subunidade_acesso_mil_and_more'),
        ('quarteis', '0006_quartel_acesso_s1_quartel_acesso_s2_and_more'),
        ('viaturas', '0002_alter_viatura_consumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='viatura',
            name='subunidade',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='viatura', to='subunidades.subunidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viatura',
            name='unidade',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='viatura', to='quarteis.quartel'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.1 on 2023-10-12 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quarteis', '0003_quartel_cidade_quartel_estado'),
        ('usuarios', '0006_alter_usuario_acesso'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='unidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='usuario', to='quarteis.quartel'),
            preserve_default=False,
        ),
    ]

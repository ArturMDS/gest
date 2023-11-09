# Generated by Django 4.2.1 on 2023-11-07 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subunidades', '0004_alter_subunidade_abreviatura'),
        ('militares', '0015_militar_data_praca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='militar',
            name='posto_grad',
            field=models.CharField(choices=[('General de Exército', 'Gen Ex'), ('General de Divisão', 'Gen Div'), ('General de Brigada', 'Gen Bda'), ('Coronel', 'Cel'), ('Tenente Coronel', 'Ten Cel'), ('Major', 'Maj'), ('Capitão', 'Cap'), ('1º Tenente', '1º Ten'), ('2º Tenente', '2º Ten'), ('Aspirante à Oficial', 'Asp Of'), ('Subtenente', 'ST'), ('1º Sargento', '1º Sgt'), ('2º Sargento', '2º Sgt'), ('3º Sargento', '3º Sgt'), ('Cabo', 'Cabo'), ('Solcado NB', 'Sd NB'), ('Soldado EV', 'Sd EV'), ('Conscrito', 'Conscrito')], default='Soldado EV', max_length=30),
        ),
        migrations.AlterField(
            model_name='militar',
            name='subunidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mil_su', to='subunidades.subunidade'),
        ),
    ]

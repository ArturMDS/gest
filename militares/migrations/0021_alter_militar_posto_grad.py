# Generated by Django 4.2.1 on 2023-12-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('militares', '0020_alter_militar_identidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='militar',
            name='posto_grad',
            field=models.CharField(choices=[('General de Exército', 'Gen Ex'), ('General de Divisão', 'Gen Div'), ('General de Brigada', 'Gen Bda'), ('Coronel', 'Cel'), ('Tenente Coronel', 'Ten Cel'), ('Major', 'Maj'), ('Capitão', 'Cap'), ('1º Tenente', '1º Ten'), ('2º Tenente', '2º Ten'), ('Aspirante à Oficial', 'Asp Of'), ('Subtenente', 'ST'), ('1º Sargento', '1º Sgt'), ('2º Sargento', '2º Sgt'), ('3º Sargento', '3º Sgt'), ('Cabo', 'Cabo'), ('Soldado NB', 'Sd NB'), ('Soldado EV', 'Sd EV'), ('Conscrito', 'Conscrito')], default='Soldado EV', max_length=30),
        ),
    ]

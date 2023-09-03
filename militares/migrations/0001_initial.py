# Generated by Django 4.2.1 on 2023-07-09 14:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Militar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_guerra', models.CharField(max_length=80)),
                ('identidade', models.CharField(blank=True, max_length=15, null=True)),
                ('numero', models.CharField(blank=True, max_length=8, null=True)),
                ('subunidade', models.CharField(choices=[('Estado Maior', 'EM'), ('Bateria Comando', 'Bia Cmdo'), ('1ª Bateria de Obuses', '1ª Bia O'), ('2ª Bateria de Obuses', '2ª Bia O'), ('3ª Bateria de Morteiros', '3ª Bia Mrt')], default='Bateria Comando', max_length=30)),
                ('posto_grad', models.CharField(choices=[('General de Exército', 'Gen Ex'), ('General de Divisão', 'Gen Div'), ('General de Brigada', 'Gen Bda'), ('Coronel', 'Cel'), ('Tenente Coronel', 'Ten Cel'), ('Major', 'Maj'), ('Capitão', 'Cap'), ('1º Tenente', '1º Ten'), ('2º Tenente', '2º Ten'), ('Aspirante à Oficial', 'Asp Of'), ('Subtenente', 'ST'), ('1º Sargento', '1º Sgt'), ('2º Sargento', '2º Sgt'), ('3º Sargento', '3º Sgt'), ('Cabo', 'Cabo'), ('Solcado NB', 'Sd NB'), ('Soldado EV', 'Sd EV')], default='Soldado EV', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Qualificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qm', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('positiva', 'FO+'), ('negativa', 'FO-'), ('neutra', 'N')], default='neutra', max_length=10)),
                ('relato_fato', models.TextField(max_length=500)),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('nr_processo', models.IntegerField(default=0)),
                ('solucao', models.CharField(choices=[('Justificado', 'Justificado'), ('Advertência de Caráter Reservado', 'ACR'), ('Advertência de Caráter Ostensivo', 'ACO'), ('Impedimento Disciplinar', 'ID'), ('Repreensão', 'Rep'), ('Detenção', 'Det'), ('Prisão', 'Prisão')], default='Justificado', max_length=50)),
                ('dias', models.IntegerField(blank=True, null=True)),
                ('publicacao_bi', models.CharField(blank=True, max_length=200, null=True)),
                ('arrolado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mil_arrolado', to='militares.militar')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mil_part', to='militares.militar')),
            ],
        ),
    ]

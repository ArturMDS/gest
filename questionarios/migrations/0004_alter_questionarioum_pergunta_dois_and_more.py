# Generated by Django 4.2.1 on 2023-11-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0003_delete_createquestionarioumform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionarioum',
            name='pergunta_dois',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questionarioum',
            name='pergunta_um',
            field=models.CharField(max_length=100),
        ),
    ]

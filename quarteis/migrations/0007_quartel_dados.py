# Generated by Django 4.2.1 on 2023-11-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quarteis', '0006_quartel_acesso_s1_quartel_acesso_s2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quartel',
            name='dados',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

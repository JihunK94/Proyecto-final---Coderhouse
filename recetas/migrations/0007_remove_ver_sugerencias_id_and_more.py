# Generated by Django 5.0.6 on 2024-06-07 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0006_alter_ver_sugerencias_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ver_sugerencias',
            name='id',
        ),
        migrations.AlterField(
            model_name='ver_sugerencias',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ver_sugerencias',
            name='numero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

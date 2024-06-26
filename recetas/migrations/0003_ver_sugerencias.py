# Generated by Django 5.0.6 on 2024-05-30 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_alter_ver_comidas_categorias_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ver_sugerencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comida_categoria_picante', models.CharField(max_length=500)),
                ('fecha_publicación', models.DateField()),
                ('sugerencia_numero', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

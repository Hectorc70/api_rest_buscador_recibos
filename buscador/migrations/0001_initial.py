# Generated by Django 3.0.2 on 2021-03-18 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('no_control', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Empleado')),
                ('apellidoP', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('apellidoM', models.CharField(max_length=100, verbose_name='Apellido Materno')),
            ],
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id_recibo', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre_archivo', models.CharField(max_length=200, verbose_name='Nombre de Archivo')),
                ('ruta_archivo', models.CharField(max_length=500, verbose_name='Ruta de Archivo')),
                ('periodo', models.CharField(max_length=6, verbose_name='Periodo')),
                ('tipo_nomina', models.CharField(max_length=100, verbose_name='Tipo de Nomina')),
                ('no_control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to='buscador.Empleado')),
            ],
        ),
    ]
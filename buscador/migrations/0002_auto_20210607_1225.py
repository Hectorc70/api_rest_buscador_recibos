# Generated by Django 3.0.2 on 2021-06-07 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='apellidoM',
            new_name='apellido_M',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='apellidoP',
            new_name='apellido_P',
        ),
    ]

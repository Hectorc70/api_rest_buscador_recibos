# Generated by Django 3.0.2 on 2021-03-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0002_auto_20210318_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='no_control',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
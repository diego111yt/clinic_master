# Generated by Django 4.2.6 on 2025-03-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_master_app', '0009_rename_imagen_empleado_firma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ips',
            name='cargos',
            field=models.TextField(help_text='Selecciona múltiples opciones separadas por comas'),
        ),
    ]

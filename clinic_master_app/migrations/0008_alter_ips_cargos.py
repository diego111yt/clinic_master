# Generated by Django 4.2.6 on 2025-03-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_master_app', '0007_contrato_archivo_empleado_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ips',
            name='cargos',
            field=models.CharField(help_text='Selecciona múltiples opciones separadas por comas', max_length=100),
        ),
    ]

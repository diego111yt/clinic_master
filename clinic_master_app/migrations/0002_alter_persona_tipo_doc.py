# Generated by Django 4.2.6 on 2025-03-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_master_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo_doc',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería')], max_length=10),
        ),
    ]

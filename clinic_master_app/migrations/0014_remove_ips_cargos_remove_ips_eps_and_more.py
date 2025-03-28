# Generated by Django 4.2.6 on 2025-03-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_master_app', '0013_remove_contrato_archivo_remove_empleado_id_contrato_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ips',
            name='cargos',
        ),
        migrations.RemoveField(
            model_name='ips',
            name='eps',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='id_especialidad',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='id_formacion',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='id_ips',
        ),
        migrations.AddField(
            model_name='empleado',
            name='especialidades',
            field=models.CharField(choices=[('Ninguno', 'ninguno'), ('Medicina General', 'Atención médica básica'), ('Cardiología', 'Enfermedades del corazón'), ('Neumología', 'Enfermedades respiratorias'), ('Gastroenterología', 'Trastornos digestivos'), ('Dermatología', 'Enfermedades de la piel'), ('Pediatría', 'Atención a niños y adolescentes'), ('Obstetricia y Ginecología', 'Salud femenina y embarazo'), ('Neurología', 'Enfermedades del sistema nervioso'), ('Oncología', 'Tratamiento del cáncer'), ('Psiquiatría', 'Trastornos mentales y emocionales'), ('Cirugía General', 'Intervenciones quirúrgicas comunes'), ('Ortopedia', 'Trastornos del sistema musculoesquelético'), ('Oftalmología', 'Enfermedades de los ojos'), ('Radiología', 'Diagnóstico por imágenes'), ('Anestesiología', 'Anestesia en procedimientos quirúrgicos')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formacion',
            name='id_empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.empleado'),
        ),
        migrations.DeleteModel(
            name='Especialidad',
        ),
        migrations.DeleteModel(
            name='Ips',
        ),
    ]

# Generated by Django 5.1.4 on 2025-04-04 12:58

import clinic_master_app.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anamnesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cirugias', models.TextField()),
                ('hospitalizacion', models.TextField()),
                ('alergias', models.TextField()),
                ('enfermedad_familiar', models.TextField()),
                ('trabajo', models.TextField()),
                ('fuma', models.TextField()),
                ('ejercicio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nivel_minimo', models.IntegerField(choices=[(1, 'Nivel 1 - Básico'), (2, 'Nivel 2 - Intermedio'), (3, 'Nivel 3 - Avanzado')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico_principal', models.TextField()),
                ('pruebas_complementarias', models.TextField()),
                ('interpretacion_examen', models.CharField(max_length=100)),
                ('diagnostico_final', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_trabajo', models.CharField(choices=[('Médico general', 'Consultorio médico'), ('Enfermero(a)', 'Área de atención a pacientes'), ('Auxiliar de enfermería', 'Área de atención a pacientes'), ('Especialistas médicos', 'Consultorio especializado'), ('Gerente médico', 'Oficina administrativa médica'), ('Gerente administrativo', 'Oficina administrativa'), ('Recepcionista', 'Recepción y gestión de citas'), ('Contador(a)', 'Departamento de contabilidad y finanzas'), ('Técnico en sistemas', 'Departamento de tecnología y soporte')], max_length=100)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Suspendido', 'Suspendido')], default='Activo', max_length=20)),
                ('puesto_empresa', models.CharField(choices=[('Puesto clínico', 'Médico general'), ('Puesto clínico', 'Enfermero(a)'), ('Puesto clínico', 'Auxiliar de enfermería'), ('Puesto clínico', 'Especialistas médicos'), ('Puesto administrativo', 'Gerente médico'), ('Puesto administrativo', 'Gerente administrativo'), ('Puesto administrativo', 'Recepcionista'), ('Puesto administrativo', 'Contador(a)'), ('Otros puestos', 'Técnico en sistemas'), ('it', 'IT')], max_length=100)),
                ('especialidades', models.CharField(choices=[('Ninguno', 'ninguno'), ('Medicina General', 'Atención médica básica'), ('Cardiología', 'Enfermedades del corazón'), ('Neumología', 'Enfermedades respiratorias'), ('Gastroenterología', 'Trastornos digestivos'), ('Dermatología', 'Enfermedades de la piel'), ('Pediatría', 'Atención a niños y adolescentes'), ('Obstetricia y Ginecología', 'Salud femenina y embarazo'), ('Neurología', 'Enfermedades del sistema nervioso'), ('Oncología', 'Tratamiento del cáncer'), ('Psiquiatría', 'Trastornos mentales y emocionales'), ('Cirugía General', 'Intervenciones quirúrgicas comunes'), ('Ortopedia', 'Trastornos del sistema musculoesquelético'), ('Oftalmología', 'Enfermedades de los ojos'), ('Radiología', 'Diagnóstico por imágenes'), ('Anestesiología', 'Anestesia en procedimientos quirúrgicos')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_eps', models.CharField(max_length=100)),
                ('direccion_eps', models.CharField(max_length=100)),
                ('telefono_eps', models.CharField(max_length=15)),
                ('email_eps', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_examen', models.CharField(max_length=100)),
                ('resultado_examen', models.TextField()),
                ('observacion_examen', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medicamento', models.CharField(max_length=100)),
                ('dosis', models.CharField(max_length=100)),
                ('frecuencia', models.CharField(max_length=100)),
                ('duracion_tratamiento', models.CharField(max_length=100)),
                ('cantidad_total', models.CharField(max_length=100)),
                ('indicaciones_especiales', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_procedimiento', models.CharField(max_length=50)),
                ('descripcion_procedimiento', models.TextField()),
                ('duracion_estimada', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sala', models.CharField(max_length=50)),
                ('ubicacion_sala', models.CharField(max_length=100)),
                ('capacidad_sala', models.CharField(max_length=100)),
                ('horario_disponible', models.DateTimeField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_contrato', models.CharField(choices=[('Médico general', 'Contrato a término indefinido'), ('Enfermero(a)', 'Contrato a término indefinido'), ('Auxiliar de enfermería', 'Contrato a término fijo'), ('Especialistas médicos', 'Contrato por prestación de servicios'), ('Gerente médico', 'Contrato a término indefinido'), ('Gerente administrativo', 'Contrato a término indefinido'), ('Recepcionista', 'Contrato a término fijo'), ('Contador(a)', 'Contrato a término indefinido'), ('Técnico en sistemas', 'Contrato por prestación de servicios')], max_length=100)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('documento_contrato', models.FileField(blank=True, null=True, upload_to=clinic_master_app.models.user_directory_path_1, verbose_name='Contrato')),
                ('id_empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cita', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.cita')),
                ('id_anamnesis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.anamnesis')),
                ('id_diagnostico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.diagnostico')),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='id_empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.empleado'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('puesto_empresa', models.CharField(choices=[('it', 'IT'), ('medico', 'Médico'), ('admin', 'Administrador')], default='it', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('empleado', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.empleado')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='id_examen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.examen'),
        ),
        migrations.CreateModel(
            name='ExploracionFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia_cardiaca', models.PositiveIntegerField(blank=True, null=True)),
                ('temperatura', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('presion_diastolica', models.PositiveIntegerField(blank=True, null=True)),
                ('saturacion_oxigeno', models.PositiveIntegerField(blank=True, null=True)),
                ('inspeccion_general', models.TextField(blank=True, null=True)),
                ('cabeza_cuello', models.TextField(blank=True, null=True)),
                ('torax_pulmones', models.TextField(blank=True, null=True)),
                ('corazon', models.TextField(blank=True, null=True)),
                ('abdomen', models.TextField(blank=True, null=True)),
                ('extremidades', models.TextField(blank=True, null=True)),
                ('sistema_nervioso', models.TextField(blank=True, null=True)),
                ('id_anamnesis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.anamnesis')),
            ],
        ),
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_formacion', models.CharField(max_length=100)),
                ('intitucion', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField(max_length=100)),
                ('fecha_fin', models.DateField(max_length=100)),
                ('titulo_obtenido', models.CharField(max_length=100)),
                ('id_empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_expiracion', models.DateField(max_length=100)),
                ('recomendaciones_medicas', models.TextField()),
                ('id_diagnostico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.diagnostico')),
                ('mid_nombre_medicamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='anamnesis',
            name='medicamentos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.medicamento'),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_doc', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería')], max_length=10)),
                ('num_doc', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField()),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=clinic_master_app.models.user_directory_path, verbose_name='imagen')),
                ('eps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.eps')),
            ],
        ),
        migrations.CreateModel(
            name='Historia_clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.consulta')),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.persona')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='id_persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.persona'),
        ),
        migrations.AddField(
            model_name='cita',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_master_app.persona'),
        ),
    ]

from django.db import models


class Eps(models.Model):
    nombre_eps  = models.CharField(max_length=100)
    direccion_eps = models.CharField(max_length=100)
    telefono_eps = models.CharField(max_length=15)
    email_eps = models.EmailField(max_length=100)

class Ips (models.Model):
    eps = models.ForeignKey(Eps, on_delete=models.CASCADE, null=True)
    nombre_ips = models.CharField(max_length=100)
    direccion_ips = models.CharField(max_length=100)
    telefono_ips = models.CharField(max_length=15)
    email_ips = models.EmailField(max_length=100)
    cargos = models.CharField(max_length=100)

class Persona(models.Model):
    tipo_doc = models.CharField(max_length=10)
    num_doc = models.CharField(max_length=10, unique=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    genero = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    eps = models.ForeignKey(Eps, on_delete=models.CASCADE, null=True)

class Contrato(models.Model):
    salario = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=100)

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=100)
    descripcion_especialidad = models.TextField()
    
class Formacion(models.Model):
    tipo_formacion = models.CharField(max_length=100)
    intitucion = models.CharField(max_length=100)
    fecha_inicio = models.DateField(max_length=100)
    fecha_fin = models.DateField(max_length=100)
    titulo_obtenido = models.CharField(max_length=100)
    
class Empleado(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    area_trabajo = models.CharField(max_length=100)
    estado = models.CharField(max_length=20,
        choices=[
            ('Activo', 'Activo'),
            ('Inactivo', 'Inactivo'),
            ('Suspendido', 'Suspendido')],default='Activo')
    id_ips = models.ForeignKey(Ips, on_delete=models.CASCADE, null=True)
    puesto_empresa = models.CharField(max_length=100)
    firma_empleado = models.CharField(max_length=100)
    id_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, null=True)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)
    id_formacion = models.ForeignKey(Formacion, on_delete=models.CASCADE, null=True)

class Cita (models.Model):
    hora = models.TimeField()
    fecha = models.DateField()
    tipo = models.CharField(max_length=100)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    
class Procedimiento(models.Model):
    nombre_procedimiento = models.CharField(max_length=50)
    descripcion_procedimiento = models.TextField()
    duracion_estimada = models.CharField(max_length=40)
    
class Sala(models.Model):
    nombre_sala = models.CharField(max_length=50)
    ubicacion_sala = models.CharField(max_length=100)
    capacidad_sala = models.CharField(max_length=100)
    horario_disponible = models.DateTimeField(max_length=100)
        
class Examen(models.Model):
    tipo_examen = models.CharField(max_length=100)
    resultado_examen = models.TextField()
    observacion_examen = models.TextField(max_length=100)
        
class Diagnostico(models.Model):
    diagnostico_principal = models.TextField()
    pruebas_complementarias = models.TextField()
    interpretacion_examen = models.CharField(max_length=100)
    diagnostico_final = models.TextField()
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE, null=True)

class Anamnesis(models.Model):
    cirugias = models.TextField()
    hospitalizacion = models.TextField()
    alergias = models.TextField()
    enfermedad_familiar = models.TextField()
    trabajo = models.TextField()
    fuma = models.TextField()
    ejercicio = models.TextField()
    medicamentos = models.TextField()
    
class ExploracionFisica(models.Model):
    id_anamnesis = models.ForeignKey(Anamnesis, on_delete=models.CASCADE, null=True)
    frecuencia_cardiaca = models.PositiveIntegerField(null=True, blank=True)  
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)  
    presion_diastolica = models.PositiveIntegerField(null=True, blank=True)  
    saturacion_oxigeno = models.PositiveIntegerField(null=True, blank=True)  
    inspeccion_general = models.TextField(blank=True, null=True)
    cabeza_cuello = models.TextField(blank=True, null=True)
    torax_pulmones = models.TextField(blank=True, null=True)
    corazon = models.TextField(blank=True, null=True)
    abdomen = models.TextField(blank=True, null=True)
    extremidades = models.TextField(blank=True, null=True)
    sistema_nervioso = models.TextField(blank=True, null=True)


class Consulta(models.Model):
    fecha = models.DateField()
    medico = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, null=True)
    id_anamnesis = models.ForeignKey(Anamnesis, on_delete=models.CASCADE, null=True)
    id_diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True)
    
class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    duracion_tratamiento = models.CharField(max_length=100)
    cantidad_total = models.CharField(max_length=100)
    indicaciones_especiales = models.TextField()
    
class Formula(models.Model):
    descripcion = models.TextField()
    id_diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True)
    mid_nombre_medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=True)
    fecha_expiracion  = models.DateField(max_length=100)
    recomendaciones_medicas = models.TextField()   
    
class Historia_clinica(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, null=True)
    
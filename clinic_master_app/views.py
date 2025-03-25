from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth import login

#region Inicio

def home(request):
    return render(request, 'home.html') 

# region usuario

# crear_usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/crear_usuario.html', {'form': form})

# listar_usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtiene todos los usuarios
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})

# eliminar usuario
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)  # Obtiene el usuario por su ID
    if request.method == 'POST':
        usuario.delete()  # Elimina el usuario de la base de datos
        return redirect('listar_usuarios')  # Redirige a la lista de usuarios después de eliminarlo
    return render(request, 'usuario/eliminar_usuario.html', {'usuario': usuario})

# actualizar usuario
def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)  # Obtiene el usuario por su ID
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)  # Pasa el usuario a la instancia del formulario
        if form.is_valid():
            form.save()  # Guarda el formulario con los datos actualizados
            return redirect('listar_usuarios')  # Redirige a la lista de usuarios después de actualizar
    else:
        form = UsuarioForm(instance=usuario)  # Carga el formulario con los datos del usuario

    return render(request, 'usuario/actualizar_usuario.html', {'form': form})

# region login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # 🔥 Verificamos si el usuario es "diego"
            if user.username == "diego":
                return redirect("home")  # Redirigir a home.html

            # Si es otro usuario, manejar redirecciones según su puesto
            if user.puesto_empresa:
                if user.puesto_empresa.puesto_empresa == "Doctor":
                    return redirect("base")
                elif user.puesto_empresa.puesto_empresa == "Administrador":
                    return redirect("base")
                else:
                    return redirect("dashboard_general")  # Otra página si no es doctor/admin
            else:
                return redirect("dashboard_general")  # Si no tiene puesto asignado

    else:
        form = LoginForm()

    return render(request, "auth/login.html", {"form": form})

#region Persona

# crear persona
def crear_persona(request):
    if request.method =='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm()
    return render(request, 'persona/crear_persona.html', {'form':form})

# listar persona
def listar_personas(request):
    persona = Persona.objects.filter(is_active=True)
    return render(request, 'persona/listar_personas.html', {'persona_list':persona})

# reactivar usuarios
def reactivar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    persona.is_active = True
    persona.save()
    return redirect('listar_personas')

# eliminar persona
def desactivar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    persona.is_active = False
    persona.save()
    return redirect('listar_personas_inactivas')

# listar personas inactivas
def listar_personas_inactivas(request):
    personas_inactivas = Persona.objects.filter(is_active=False)
    return render(request, 'persona/listar_personas_inactivas.html', {'personas_inactivas': personas_inactivas})


# actualizar persona
def actualizar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listar_personas')  # Redirige a la lista después de actualizar
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'persona/actualizar_persona.html', {'form': form})
    
# region ips

# crear ips
def crear_ips(request):
    if request.method =='POST':
        form = IpsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ips')
    else:
        form = IpsForm()
    return render(request, 'ips/crear_ips.html', {'form':form})

# listar ips
def listar_ips(request):
    ips = Ips.objects.all()
    return render(request, 'ips/listar_ips.html',{'listar_ips':ips})

# actualizar ips
def actualizar_ips(request, ips_id):
    ips = get_object_or_404(Ips, id=ips_id)

    if request.method == 'POST':
        form = IpsForm(request.POST, instance=ips)
        if form.is_valid():
            form.save()
            return redirect('lista_ips')  # Redirige a la lista de IPS después de actualizar
    else:
        form = IpsForm(instance=ips)

    return render(request, 'actualizar_ips.html', {'form': form})

# eliminar ips
def eliminar_ips(request, ips_id):
    ips = get_object_or_404(Ips, id=ips_id)
    ips.delete()
    return redirect('listar_ips')


#region eps

# crear eps
def crear_eps(request):
    if request.method =='POST':
        form = EpsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eps')
    else:
        form = EpsForm()
    return render(request, 'eps/crear_eps.html', {'form':form})

# listar eps
def listar_eps(request):
    eps = Eps.objects.all()
    return render(request, 'eps/listar_eps.html',{'listar_eps':eps})

# actualizar eps
def actualizar_eps(request, eps_id):
    eps = get_object_or_404(Eps, id=eps_id)

    if request.method == 'POST':
        form = EpsForm(request.POST, instance=eps)
        if form.is_valid():
            form.save()
            return redirect('lista_eps')  # Redirige a la lista de EPS después de actualizar
    else:
        form = EpsForm(instance=eps)

    return render(request, 'eps/actualizar_eps.html', {'form': form})

# eliminar eps
def eliminar_eps(request, eps_id):
    eps = get_object_or_404(Eps, id=eps_id)
    eps.delete()
    return redirect('listar_eps')


# region Contrato

# crear_contrato
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')  # Redirige a la lista de contratos después de crear
    else:
        form = ContratoForm()

    return render(request, 'contrato/crear_contrato.html', {'form': form})


# listar_contrato
def listar_contratos(request):
    contratos = Contrato.objects.all()  # Obtenemos todos los registros de Contratos
    return render(request, 'contrato/listar_contratos.html', {'listar_contratos': contratos})


# actualizar_contrato
def actualizar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)

    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos')  # Redirige a la lista de contratos después de actualizar
    else:
        form = ContratoForm(instance=contrato)

    return render(request, 'contrato/actualizar_contrato.html', {'form': form})

# eliminar contrata
def eliminar_contrato(request, contrato_id):
    contrato = get_object_or_404(Contrato, id=contrato_id)
    contrato.delete()
    return redirect('listar_contratos')


# region Especialidad

# crear
def crear_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_especialidades')  # Redirige a la lista de especialidades después de crear
    else:
        form = EspecialidadForm()

    return render(request, 'especialidad/crear_especialidad.html', {'form': form})



# listar
def listar_especialidades(request):
    especialidades = Especialidad.objects.all()  # Obtenemos todos los registros de Especialidades
    return render(request, 'especialidad/listar_especialidades.html', {'listar_especialidades': especialidades})

# actualizar
def actualizar_especialidad(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, id=especialidad_id)

    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('listar_especialidades')  # Redirige a la lista de especialidades después de actualizar
    else:
        form = EspecialidadForm(instance=especialidad)

    return render(request, 'especialidad/actualizar_especialidad.html', {'form': form})

# eliminar especialidad
def eliminar_especialidad(request, especialidad_id):
    especialidad = get_object_or_404(Especialidad, id=especialidad_id)
    especialidad.delete()
    return redirect('listar_especialidades')



# region Formacion


# crear
def crear_formacion(request):
    if request.method == 'POST':
        form = FormacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_formaciones')  # Redirige a la lista de formaciones después de crear
    else:
        form = FormacionForm()

    return render(request, 'formacion/crear_formacion.html', {'form': form})

# listar
def listar_formaciones(request):
    formaciones = Formacion.objects.all()  # Obtenemos todos los registros de Formaciones
    return render(request, 'formacion/listar_formaciones.html', {'listar_formaciones': formaciones})

# actuaizar
def actualizar_formacion(request, formacion_id):
    formacion = get_object_or_404(Formacion, id=formacion_id)

    if request.method == 'POST':
        form = FormacionForm(request.POST, instance=formacion)
        if form.is_valid():
            form.save()
            return redirect('listar_formacion')  # Redirige a la lista de formaciones después de actualizar
    else:
        form = FormacionForm(instance=formacion)

    return render(request, 'formacion/actualizar_formacion.html', {'form': form})

# eliminar formacion
def eliminar_formacion(request, formacion_id):
    formacion = get_object_or_404(Formacion, id=formacion_id)
    formacion.delete()
    return redirect('listar_formaciones')
#region empleado

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/crear_empleado.html', {'form': form})

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/listar_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/actualizar_empleado.html', {'form': form})

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    empleado.delete()
    return redirect('listar_empleados')


# region Citas

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm()
    return render(request, 'cita/crear_cita.html', {'form': form})

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'cita/listar_citas.html', {'citas': citas})

def actualizar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'cita/actualizar_cita.html', {'form': form})

def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    cita.delete()
    return redirect('listar_citas')




# region Procedimiento
# crear procedimiento
def crear_procedimiento(request):
    if request.method == 'POST':
        form = ProcedimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_procedimientos')  # Redirige a la lista de procedimientos después de crear
    else:
        form = ProcedimientoForm()

    return render(request, 'procedimiento/crear_procedimiento.html', {'form': form})


# listar procedimiento
def listar_procedimiento(request):
    procedimientos = Procedimiento.objects.all()
    return render(request, 'procedimiento/listar_procedimiento.html', {'listar_procedimiento': procedimientos})

# actualizar procedimiento
def actualizar_procedimiento(request, procedimiento_id):
    procedimiento = get_object_or_404(Procedimiento, id=procedimiento_id)

    if request.method == 'POST':
        form = ProcedimientoForm(request.POST, instance=procedimiento)
        if form.is_valid():
            form.save()
            return redirect('listar_procedimientos')  # Redirige a la lista de procedimientos después de actualizar
    else:
        form = ProcedimientoForm(instance=procedimiento)

    return render(request, 'procedimiento/actualizar_procedimiento.html', {'form': form})

# eliminar procedimiento
def eliminar_procedimiento(request, procedimiento_id):
    procedimiento = get_object_or_404(Procedimiento, id=procedimiento_id)
    procedimiento.delete()
    return redirect('listar_procedimientos')


# region Salas


def crear_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_salas')
    else:
        form = SalaForm()
    return render(request, 'sala/crear_sala.html', {'form': form})

def listar_salas(request):
    salas = Sala.objects.all()
    return render(request, 'sala/listar_salas.html', {'salas': salas})

def actualizar_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('listar_salas')
    else:
        form = SalaForm(instance=sala)
    return render(request, 'sala/actualizar_sala.html', {'form': form})

def eliminar_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    sala.delete()
    return redirect('listar_salas')


# region Examenes


def crear_examen(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_examenes')
    else:
        form = ExamenForm()
    return render(request, 'examen/crear_examen.html', {'form': form})

def listar_examenes(request):
    examenes = Examen.objects.all()
    return render(request, 'examen/listar_examenes.html', {'examenes': examenes})

def actualizar_examen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    if request.method == 'POST':
        form = ExamenForm(request.POST, instance=examen)
        if form.is_valid():
            form.save()
            return redirect('listar_examenes')
    else:
        form = ExamenForm(instance=examen)
    return render(request, 'examen/actualizar_examen.html', {'form': form})

def eliminar_examen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    examen.delete()
    return redirect('listar_examenes')


# region Diagnosticos

def crear_diagnostico(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_diagnosticos')
    else:
        form = DiagnosticoForm()
    return render(request, 'diagnostico/crear_diagnostico.html', {'form': form})

def listar_diagnosticos(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'diagnostico/listar_diagnosticos.html', {'diagnosticos': diagnosticos})

def actualizar_diagnostico(request, diagnostico_id):
    diagnostico = get_object_or_404(Diagnostico, id=diagnostico_id)
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST, instance=diagnostico)
        if form.is_valid():
            form.save()
            return redirect('listar_diagnosticos')
    else:
        form = DiagnosticoForm(instance=diagnostico)
    return render(request, 'diagnostico/actualizar_diagnostico.html', {'form': form})

def eliminar_diagnostico(request, diagnostico_id):
    diagnostico = get_object_or_404(Diagnostico, id=diagnostico_id)
    diagnostico.delete()
    return redirect('listar_diagnosticos')



# region Anamnesis
# crear anamnesis
def crear_anamnesis(request):
    if request.method == 'POST':
        form = AnamnesisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_anamnesis')  # Redirige a la lista de anamnesis después de crear
    else:
        form = AnamnesisForm()

    return render(request, 'anamnesis/crear_anamnesis.html', {'form': form})

# listar anamnesis
def listar_anamnesis(request):
    anamnesis = Anamnesis.objects.all()
    return render(request, 'anamnesis/listar_anamnesis.html', {'listar_anamnesis': anamnesis})

# actualizar anamnesis
def actualizar_anamnesis(request, anamnesis_id):
    anamnesis = get_object_or_404(Anamnesis, id=anamnesis_id)

    if request.method == 'POST':
        form = AnamnesisForm(request.POST, instance=anamnesis)
        if form.is_valid():
            form.save()
            return redirect('listar_anamnesis')  # Redirige a la lista de anamnesis después de actualizar
    else:
        form = AnamnesisForm(instance=anamnesis)

    return render(request, 'anamnesis/actualizar_anamnesis.html', {'form': form})
# eliminar anamnesis
def eliminar_anamnesis(request, anamnesis_id):
    anamnesis = get_object_or_404(Anamnesis, id=anamnesis_id)
    anamnesis.delete()
    return redirect('listar_anamnesis')

# region Exploración Física
# crear exploracion fisica
def crear_exploracion_fisica(request):
    if request.method == 'POST':
        form = ExploracionFisicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_exploraciones')
    else:
        form = ExploracionFisicaForm()
    return render(request, 'exploracion/crear_exploracion.html', {'form': form})

# listar ecploracion fisica
def listar_exploraciones_fisica(request):
    exploraciones = ExploracionFisica.objects.all()
    return render(request, 'exploracion/listar_exploraciones.html', {'exploraciones': exploraciones})

def actualizar_exploracion_fisica(request, exploracion_id):
    exploracion = get_object_or_404(ExploracionFisica, id=exploracion_id)
    if request.method == 'POST':
        form = ExploracionFisicaForm(request.POST, instance=exploracion)
        if form.is_valid():
            form.save()
            return redirect('listar_exploraciones')
    else:
        form = ExploracionFisicaForm(instance=exploracion)
    return render(request, 'exploracion/actualizar_exploracion.html', {'form': form})

def eliminar_exploracion_fisica(request, exploracion_id):
    exploracion = get_object_or_404(ExploracionFisica, id=exploracion_id)
    exploracion.delete()
    return redirect('listar_exploraciones')

# region Consultas

# crear consulta
def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'consulta/crear_consulta.html', {'form': form})

# listar consultas
def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/listar_consultas.html', {'consultas': consultas})

# actualizar consulta
def actualizar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'consulta/actualizar_consulta.html', {'form': form})

# eliminar consulta
def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.delete()
    return redirect('listar_consultas')
    
# region Medicamento
# crear medicamento
def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicamentos')  # Redirige a la lista de medicamentos después de crear
    else:
        form = MedicamentoForm()

    return render(request, 'medicamento/crear_medicamento.html', {'form': form})

# listar medicamento
def listar_medicamento(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamento/listar_medicamento.html', {'listar_medicamento': medicamentos})

# actualizar medicamento
def actualizar_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, id=medicamento_id)

    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('listar_medicamentos')  # Redirige a la lista de medicamentos después de actualizar
    else:
        form = MedicamentoForm(instance=medicamento)

    return render(request, 'medicamento/actualizar_medicamento.html', {'form': form})

# eliminar medicamento
def eliminar_medicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, id=medicamento_id)
    medicamento.delete()
    return redirect('listar_medicamentos')




# region Formula
# crear formula
def crear_formula(request):
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_formulas')  # Redirige a la lista de fórmulas después de crear
    else:
        form = FormulaForm()

    return render(request, 'formula/crear_formula.html', {'form': form})

# listar formula
def listar_formula(request):
    formulas = Formula.objects.all()
    return render(request, 'formula/listar_formula.html', {'listar_formula': formulas})

# actualizar formula
def actualizar_formula(request, formula_id):
    formula = get_object_or_404(Formula, id=formula_id)

    if request.method == 'POST':
        form = FormulaForm(request.POST, instance=formula)
        if form.is_valid():
            form.save()
            return redirect('listar_formulas')  # Redirige a la lista de fórmulas después de actualizar
    else:
        form = FormulaForm(instance=formula)

    return render(request, 'formula/actualizar_formula.html', {'form': form})

# eliminar formula
def eliminar_formula(request, formula_id):
    formula = get_object_or_404(Formula, id=formula_id)
    formula.delete()
    return redirect('listar_formulas')



# region  Historia Clínica

def crear_historia_clinica(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_historias_clinicas')
    else:
        form = HistoriaClinicaForm()
    return render(request, 'historia_clinica/crear_historia_clinica.html', {'form': form})

def listar_historias_clinicas(request):
    historias = Historia_clinica.objects.all()
    return render(request, 'historia_clinica/listar_historias_clinicas.html', {'historias': historias})

def actualizar_historia_clinica(request, historia_id):
    historia = get_object_or_404(Historia_clinica, id=historia_id)
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST, instance=historia)
        if form.is_valid():
            form.save()
            return redirect('listar_historias_clinicas')
    else:
        form = HistoriaClinicaForm(instance=historia)
    return render(request, 'historia_clinica/actualizar_historia_clinica.html', {'form': form})

def eliminar_historia_clinica(request, historia_id):
    historia = get_object_or_404(Historia_clinica, id=historia_id)
    historia.delete()
    return redirect('listar_historias_clinicas')
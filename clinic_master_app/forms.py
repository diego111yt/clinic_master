from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm,UserCreationForm
from django_select2.forms import Select2MultipleWidget
from django.contrib.auth import authenticate
from django_select2.forms import ModelSelect2Widget

CARGOS = [
    ("medico_general", "Médico General"),
    ("medico_especialista", "Médico Especialista"),
    ("enfermero_jefe", "Enfermero(a) Jefe"),
    ("auxiliar_enfermeria", "Auxiliar de Enfermería"),
    ("terapista", "Terapista (Físico, Ocupacional, Respiratorio, etc.)"),
    ("bacteriologo", "Bacteriólogo(a)"),
    ("director_medico", "Gerente o Director Médico"),
    ("coordinador_salud", "Coordinador de Servicios de Salud"),
    ("recepcionista", "Recepcionista / Auxiliar Administrativo"),
    ("facturador", "Facturador o Auxiliar de Cuentas Médicas"),
    ("trabajador_social", "Trabajador Social"),
    ("regente_farmacia", "Regente de Farmacia"),
    ("tecnico_radiologia", "Técnico en Radiología"),
    ("aseo_mantenimiento", "Personal de Aseo y Mantenimiento"),
]

# region login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

# region  usuario form
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["persona","username", "puesto_empresa", "password1", "password2"]

class UsuarioUpdateForm(UserChangeForm):
    password = None  # Oculta el campo de contraseña

    class Meta:
        model = Usuario
        fields = ['persona', 'username', 'puesto_empresa']



# region eps form
class EpsForm(forms.ModelForm):
    class Meta:
        model = Eps
        fields = '__all__'
        
# region persona form
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'fecha_nac': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr'}),
        }

# region contrato form
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'


# region formacion form
class FormacionForm(forms.ModelForm):
    class Meta:
        model = Formacion
        fields = '__all__'


# region empleado form
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

# region cita form
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {            
            
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'flatpickr'}
            ),
            'hora': forms.TimeInput(
                format='%H:%M',  # ✅ 24 horas con formato 00:00
                attrs={
                    'class': 'flatpickr-time',
                    'placeholder': '00:00',
                    'style': 'width: 180px; font-size: 16px; padding: 5px; text-align: center;',
                }
            ),
            
        }
        
# region procedimiento form
class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        fields = '__all__'


# region sala form
class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'


# region examen form
class ExamenForm(forms.ModelForm):
    
    class Meta:
        model = Examen
        fields = '__all__'

# region diagnostico form
class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = '__all__'

# region anamnesis form
class AnamnesisForm(forms.ModelForm):
    class Meta:
        model = Anamnesis
        fields = '__all__'

# region exploracion_fisica form
class ExploracionFisicaForm(forms.ModelForm):
    class Meta:
        model = ExploracionFisica
        fields = '__all__'

# region consulta form
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

# region medicamento form
class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'

# region formula form
class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = '__all__'

# region historia clinica form
class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = Historia_clinica
        fields = '__all__'

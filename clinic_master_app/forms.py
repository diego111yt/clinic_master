from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','password1', 'password2', 'empleado']






class EpsForm(forms.ModelForm):
    class Meta:
        model = Eps
        fields = '__all__'

class IpsForm(forms.ModelForm):
    class Meta:
        model = Ips
        fields = '__all__'

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'fecha_nac': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'flatpickr'})
        }

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class FormacionForm(forms.ModelForm):
    class Meta:
        model = Formacion
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        fields = '__all__'

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class ExamenForm(forms.ModelForm):
    
    class Meta:
        model = Examen
        fields = '__all__'

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = '__all__'

class AnamnesisForm(forms.ModelForm):
    class Meta:
        model = Anamnesis
        fields = '__all__'

class ExploracionFisicaForm(forms.ModelForm):
    class Meta:
        model = ExploracionFisica
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'

class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = '__all__'

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = Historia_clinica
        fields = '__all__'

from django.apps import AppConfig


class ClinicMasterAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clinic_master_app'
    
    def ready(self):
        import clinic_master_app.signals
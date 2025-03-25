from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_migrate)
def create_default_user(sender, **kwargs):
    Usuario = get_user_model()
    # Verifica si el usuario 'diego' ya existe
    if not Usuario.objects.filter(username='diego').exists():
        Usuario.objects.create_user(username='diego', password='111')
        print('✅ Usuario "diego" creado con éxito.')
    else:
        print('⚠️ El usuario "diego" ya existe.')
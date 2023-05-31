import os
import django
from apps.user.models import Role
from django.conf import settings

settings.configure()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()


def create_roles():
    roles = ['administrador', 'blogger']
    for rol in roles:
        role, created = Role.objects.get_or_create(name=rol)


create_roles()

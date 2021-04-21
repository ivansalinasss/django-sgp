from django.urls import path

from administracion.views import *
from webinf.views import *

urlpatterns = [
    path('usuarios/', usuarios, name='usuarios'),
    path('crearRoles/', crearRoles, name='crearRoles'),
    path('register/', register, name='crearUsuarios')
]
from django.urls import path

from modulos.administracion.views import *
from modulos.webinf.views import *

urlpatterns = [
    path('usuarios/', usuarios, name='usuarios'),
    path('crearRoles/', crearRoles, name='crearRoles'),
    path('register/', register, name='crearUsuarios')
]
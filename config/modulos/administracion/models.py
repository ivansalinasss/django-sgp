import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Rol(models.Model):
    """
    Roles
    """
    codigo = models.CharField(
        max_length=50,
        verbose_name='Codigo',
        unique=True
    )

    descripcion = models.CharField(
        max_length=150,
        verbose_name='Descripcion'
    )

    cracion= models.DateTimeField(
        default=datetime.timezone.now,
        verbose_name='Fecha y hora creacion'
    )

    class Meta:
        verbose_name='Rol'
        verbose_name_plural='Roles'
        db_table='empleado'
        ordering=['codigo']


class Usuario(AbstractUser):
    """
    Usuarios
    """
    roles = models.ManyToManyField(
        Rol,
        verbose_name='Roles'
    )

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='usuario'
        ordering=['id']


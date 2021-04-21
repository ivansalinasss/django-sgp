from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group


# Create your models here.
class Rol(Group):

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

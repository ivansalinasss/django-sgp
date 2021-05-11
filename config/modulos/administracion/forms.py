from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from modulos.administracion.models import Usuario


class UserForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ('username', 'email')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'})
        }

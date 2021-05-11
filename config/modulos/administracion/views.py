from django.shortcuts import render, redirect

# Create your views here.
from modulos.administracion.forms import UserForm


def usuarios(request):
    return render(request, '../templates/usuarios.html')


def crearRoles(request):
    return render(request, '../templates/crearRoles.html')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print('ingresado')
            form.save()
            return redirect('webinf:dashboard')
        else:
            print(form.errors)
            return render(request, '../templates/crearUsuario.html', {'form': form})
    else:
        context = {
            'form': form
        }
        return render(request, '../templates/crearUsuario.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.


def usuarios(request):
    return render(request, 'usuarios.html')


def crearRoles(request):
    return render(request, 'crearRoles.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        return redirect('')

    else:
        return render(request, 'crearUsuario.html')

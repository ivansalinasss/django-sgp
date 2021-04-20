from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def dashboard(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')

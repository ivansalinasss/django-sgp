from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'index.html')
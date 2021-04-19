from django.urls import path
from modulos.webinf.views import *

urlpatterns = [
    path('login/', login),
    path('', dashboard)
]
from django.urls import path
from modulos.webinf.views import *

app_name = 'webinf'

urlpatterns = [
    path('login/', login, name='login'),
    path('', dashboard, name='dashboard')
]
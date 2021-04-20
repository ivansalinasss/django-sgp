from django.urls import path
from webinf.views import *

urlpatterns = [
    path('login/', login),
    path('', dashboard)
]
from django.shortcuts import render

from . import models

# Create your views here.

def lista_clientes(request):
    persons = models.Clientes.objects.all()
    # cli = models.Clientes.objects.get()
    return render(request, 'clientes.html', {'persons':persons})
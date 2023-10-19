from django.shortcuts import render, redirect
from . import forms

from . import models

# Create your views here.

def lista_clientes(request):
    persons = models.Clientes.objects.all()
    # cli = models.Clientes.objects.get()
    return render(request, 'clientes.html', {'persons':persons})


def add_cliente(request):
    form = forms.ClienteForm(request.POST, request.FILES , None)
    if form.is_valid():
        form.save()
        return redirect('mostra_clientes')
    return render(request, 'cliente_form.html', {'form':form})
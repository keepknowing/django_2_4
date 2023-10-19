from django.forms import ModelForm
from . import models

class ClienteForm(ModelForm):
    class Meta:
        model = models.Clientes
        fields = ['nome', 'sobrenome','cpf','email','photo']

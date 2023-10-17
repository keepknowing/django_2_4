from django.db import models

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    # nascimento = models.DateField()
    # socio = models.BooleanField()
    cpf = models.CharField(max_length=11, help_text='CPF - Apenas Números')
    email = models.EmailField(max_length=80)


    def __str__(self) -> str:
        return '{} {}'.format(self.nome.title(),self.sobrenome.title())

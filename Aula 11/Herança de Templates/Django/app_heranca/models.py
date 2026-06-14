from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100) #Definir campo, tipo e comprimento
    cpf = models.CharField(max_length=14, unique=True) #unique=True -> Determina unico cpf por pessoa
    telefone = models.CharField(max_length=20)

    # METODO PARA EXIBIR OS CLIENTES
    def __str__(self):
        return self.nome
    


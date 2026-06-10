from django.db import models

# Create your models here.

class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=20)
    turma = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


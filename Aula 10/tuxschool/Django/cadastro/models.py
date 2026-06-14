from django.db import models

# Create your models here.

class Campus(models.Model):
    nome = models.CharField(max_length=100)

    #cria o atributo aluno e cria a relação
    aluno = models.ForeignKey(Aluno)

    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=20)
    turma = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    
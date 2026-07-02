from django.db import models

# Create your models here.
class Livro(models.Model):
        titulo = models.CharField(max_length=50)
        autor = models.CharField(max_length=50)
        categoria = models.CharField(max_length=50)
        qtd_disponivel = models.IntegerField(default=0)
        
        def __str__(self):
            return f'{self.titulo} de {self.autor} - Quantidade: {self.qtd_disponivel}'
        
        def emprestar(self):
            if self.quantidade > 0:
                self.quantidade -= 1
                self.save()
                return True
            return False
        
        def devolver(self):
            self.quantidade += 1
            self.save()


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'
    

class Conta(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #senha = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Conta {self.numero} - {self.usuario.nome}'

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    devolvido = models.BooleanField(default=False) # False = ainda não devolveu

    def __str__(self):
        return f'Nome: {self.usuario} - Livro: {self.livro} - Data Empréstimo: {self.data_emprestimo} - Devolução: {self.devolvido}'
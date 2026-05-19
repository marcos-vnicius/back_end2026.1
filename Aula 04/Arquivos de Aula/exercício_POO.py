# Atributos: características / informações do objeto
# Métodos: ações do objeto

"""
1º : criar classe
2º : os métodos ( def ação(self) ) ou atributos ( self.atributo = atributo)
3º : criar a variável que vai receber a classe e definir seus atributos
     ou definir os métodos:
     ( Aluno_1 = Aluno("Marcos", 25) ) (  )
"""

class Animal:
    def latir(self):
        print("AU AU")

class Computador:
    def ligar(self):
        print("ligando...")

class Celular:
    def digitar(self):
        print("Digitando...")

class Aluno:
    # __init__ -> Método construtor: tudo que estiver dentro dele -
    #              - será criado automaticamente
    def __init__(self, nome, idade):

        # Atributos
        self.nome = nome
        self.idade = idade

Aluno_1 = Aluno("Marcos", 25)
Aluno_2 = Aluno("Bruno", 22)

print("Aluno 1:")
print(f"Nome: {Aluno_1.nome}")
print(f"Idade: {Aluno_1.idade} anos")
print(20*"-")
print("Aluno 2:")
print(f"Nome: {Aluno_2.nome}")
print(f"Idade: {Aluno_2.idade} anos")
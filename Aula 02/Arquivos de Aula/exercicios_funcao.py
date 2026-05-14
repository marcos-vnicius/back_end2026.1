""" Criando e executando funções """

#Função criada
""" def fazer_cafe():
    print("Café Pronto!")

#Chama a função
fazer_cafe() """

#------------------------------------

#DESAFIO 01
""" def mensagem():
    print("Bem-vindo ao Sistema!")

mensagem() """

#------------------------------------

#DESAFIO 02
""" def saudacao():
    print("Bem-vindo!")

def menu():
    print("1 - Pastel")
    print("2 - Hambúrguer")
    print("3 - Pizza")

def linha():
    print(15*"-")

saudacao()
linha()
menu() """

#-----------------------------------

""" def ola(nome):
    print(f"Olá, {nome}")

nome_usuario = input("Qual o seu nome? : ")
nome_usuario_dois = input("Qual o seu nome? : ")

ola(nome_usuario)
ola(nome_usuario_dois) """

#-----------------------------------

#Desafio 03
""" def mostrar_idade(idade):
    print(20*"-")
    print(f"Sua idade é {idade} anos")

def mostrar_cidade(cidade):
    print(20*"-")
    print(f"Sua cidade é {cidade}")

def mostrar_produtos(produtos):
    print(20*"-")
    print("Nossos Produtos:")
    print(produtos)

idade_usuario = input("Informe sua idade: ")
cidade_usuario = input("Informe sua cidade: ")

mostrar_idade(idade_usuario)
mostrar_cidade(cidade_usuario)
mostrar_produtos("Televisão | Video Game | SmartWatch") """

#-----------------------------------

#Desafio 03
""" def mostrar_dados_usuario(nome, idade):
    print(f"{nome} tem {idade} anos")

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

mostrar_dados_usuario(nome, idade) """

#-----------------------------------

#Desafio 04
""" def cadastrar_produto(produto_cadastrado):
    print(f"O Produto {produto_cadastrado} cadastrado!")

def informar_venda(produto_vendido):
    print(f"O produto {produto_vendido} foi vendido!")

def resultado_soma(num_1, num_2):
    resultado = num_1 + num_2
    print(f"A soma dos número {num_1} e {num_2} é igual a: {resultado}")

#cadastro
cadastrar_produto("Relógio")

#venda
informar_venda("Relógio")

#soma
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
resultado_soma(num_1, num_2) """
from django.shortcuts import render

 # Importar a classe (ferramenta) HttpResponse
from django.http import HttpResponse # Vai responder a solicitação do navegaor

 # Cria a função que responde a solicitação do navegador
def ola_mundo(request):
    return HttpResponse("Olá Mundo!")

def contato(request):
    return render(request, "clientes/contato.htm",)


 # Chamar arquivos HTML (Template)
def home(request):
    # Conceito de context (contexto)
    #Context -> pega os dados na view e passa para o template
    titulo = "Nossos Melhores Clientes"
    nosso_cliente = {
        'nome': 'Marcos',
        'idade': 25,
        'nascimento': '31/03/2001'
    }

    nomes_clientes = ['Maria', 'João', 'Matheus', 'Ana']

    carros = [
        {'marca': 'Chevrolet', 'modelo': 'Onix LT', 'ano': '2020'},
        {'marca': 'Fiat', 'modelo': 'Uno', 'ano': '2010'},
    ]

    return render(request, "clientes/home.html", {'mensagem':titulo, 'lista_clientes':nosso_cliente, 'dados':nomes_clientes, 'meus_carros':carros},)

def formulario(request):
    return render(request, "clientes/formulario.html" )
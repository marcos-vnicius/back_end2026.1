from django.shortcuts import render

 # Importar a classe (ferramenta) HttpResponse
from django.http import HttpResponse # Vai responder a solicitação do navegaor

 # Cria a função que responde a solicitação do navegador
def ola_mundo(request):
    return HttpResponse("Olá Mundo!")

def contato(request):
    return HttpResponse(" <form> <label>Email: </label><input type=text> </form>\n <form> <label>Telefone: </label><input type=text> </form> ")

from django.shortcuts import render

# Create your views here.

# Função da página Inicial
def index(request):
    return render(request, 'pages/home.html')

def abrir_conta(request):
    return render(request, 'pages/abrir_conta.html')
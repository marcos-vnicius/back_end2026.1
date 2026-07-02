from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from decimal import Decimal
from .models import Livro, Usuario, Conta, Emprestimo
import random
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

def cadastro_usuario(request):
    if request.method == "POST":
        nome_form = request.POST.get('nome_usuario')
        email_form = request.POST.get('email')

        if Usuario.objects.filter(email=email_form).exists():
            messages.error(request, 'E-mail já cadastrado! Use outro e-mail ou acesse uma conta existente.')
            return render(request, 'pages/cad_usuario.html')
        try:
            usuario = Usuario.objects.create(nome=nome_form, email=email_form)
            numero = (random.randint(1000, 99999))

            while Conta.objects.filter(numero=numero).exists():
                numero = str(random.randint(10000, 99999))

            conta = Conta.objects.create(numero=numero, usuario=usuario)

            messages.success(request, f'Conta criada com sucesso! Seu numero de conta é: {numero}')

            request.session['conta_numero'] = numero

            return redirect('conta', conta_id=conta.id)

        except IntegrityError:
            messages.error(request, f'Erro ao cadastrar usuário. Este e-mail já foi cadastrado')
            return render(request, 'pages/cad_usuario.html')

        except Exception as e:
            messages.error(request, f'Houve um erro ao cadastrar usuário: {str(e)}') 
            return render(request, 'pages/cad_usuario.html')

    return render(request, 'pages/cad_usuario.html')

def cad_livros(request):
    return render(request, 'pages/cad_livros.html')

def conta(request, conta_id):
    return render(request, 'pages/conta.html')


def emprestimos(request):
    return render(request, 'pages/emprestimos.html')

def listar_livros(request):
    return render(request, 'pages/listar_livros.html')

def listar_usuarios(request):
    return render(request, 'pages/listar_usuarios.html')
        

from django.shortcuts import render

def home(request):
    titulo = "Página Inicial"
    return render(request,'cadastros/home.html', {'titulo_home':titulo})

def tabela_alunos(request):
    titulo = "Alunos Cadastrados"
    lista_alunos = [
        {'nome':'Marcos', 'curso':'Python', 'turma':'2026.1'},
        {'nome':'Anna', 'curso':'Django', 'turma':'2026.2'},
        {'nome':'Carlos', 'curso':'JavaScript', 'turma':'2026.3'},
    ]

    return render(request, 'cadastros/alunos.html', {'list_alunos':lista_alunos, 'msg':titulo} )


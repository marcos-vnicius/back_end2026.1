biblioteca = []
emprestimos = []

def mensagem(msg):
    print(msg)

def menu():
    mensagem("==== Biblioteca do Python ====")
    mensagem("1 - Cadastrar livros\n2- Mostrar livros disponíveis\n3 - Registrar empréstimo\n4 - Mostrar quantidade emprestada\n5 - Sair")

def cadastrar_livro():
    nome_livro = input("Nome do livro: ")
    biblioteca.append(nome_livro)
    mensagem("Livro cadastrado")

def mostrar_livros():
    mensagem("\n==== LIVROS ====")
    for i in range(len(biblioteca)):
        mensagem(f"{i} - {biblioteca[i]}")

def emprestimo():
    mostrar_livros()
    escolha = int(input("Escolha o livro pelo número"))
    emprestimos.append(escolha)
    mensagem("Livro emprestado com sucesso!")

def total_emprestimo():
    len(emprestimos)


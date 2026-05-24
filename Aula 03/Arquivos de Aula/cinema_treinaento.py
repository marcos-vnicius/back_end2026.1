lista_salgados = []
lista_precos = []

# --- Função de mensagem ---
def mensagem(msg):
    print(msg)

# --- Função cadastrar salgado ---
def cadastrar_salgados():
    while True:
        nome_salgado = input("Informe o nome do salgado: ")
        preco_salgado = input("Informe o preco do salgado: ")

        lista_salgados.append(nome_salgado)
        lista_precos.append(preco_salgado)

        mensagem("Salgado cadastrado com sucesso!")
        

# --- Função Consultar Sabores ---
def salgados_disponiveis():
    mensagem(f"Salgados Disponíveis:")
    for i in range(len(lista_salgados)):
        mensagem(f"{i} - {lista_salgados[i]} - R$ {lista_precos[i]}")

# --- Função --- 

# --- Função Menu ---
def menu():
    mensagem(f" --- Ribeiro Salgados ---\n1 - Cadastrar Salgados\n2 - Salgados Disponíveis\n3 - Fazer Pedido\n4 - Sair\n{20*"-"}")
    opcao = int(input("Escolha uma opção [1] [2] [3] [4]: "))
    if opcao == 1:
        cadastrar_salgados()
    elif opcao == 2:
        mensagem("salgados_disponiveis()")
    elif opcao == 3:
        mensagem("fazer_pedido()")
    elif opcao == 4:
        mensagem("break")
    else:
        mensagem("[Opção Inválida]")
    
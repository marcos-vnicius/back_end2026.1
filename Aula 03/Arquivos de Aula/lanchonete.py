#Sistema Lanchonete
 
#Define as listas
lanches = []
precos = []
pedidos = []
 
#Função de mensagens
def mensagem(msg):
    print(msg)
 
#Função cadastrar lanche
def cadastrar_lanche(lanche, preco):
    #append cadastro itens na lista
    lanches.append(lanche)
    precos.append(preco)
    return mensagem("Lanche cadastrado")
 
#Função mostrar cardápio
def mostrar_cardapio():
    for i in range(len(lanches)):
        mensagem(f"{i} - {lanches[i]} - R${precos[i]}")
 
#Função fazer pedido
def fazer_pedido(pedido):
    pedidos.append(precos[pedido])


#Calcula total de pedidos
def calcular_total():
    return sum(pedidos)

def menu():
    print("\n==== Lanchonete do Python ====")
    print("1 - Cadastrar Lanche\n2- Mostrar cardápio\n3 - Fazer pedido\n 4 - Mostrar total\n 5 - Sair ")
    
#Aqui acontece a mágica
def main():
    while True:
        menu()
        opcao = int(input("Escolha seu lanche pelo número: "))
        if opcao == 1:
            lanche = input("Nome do lanche: ")
            preco = float(input("Informe o Preço: R$"))
            cadastrar_lanche(lanche, preco)
            mensagem("Lanche cadstrado com sucesso!")
        elif opcao == 2:
            mensagem("\n==== Cardápio ====")
            mostrar_cardapio()
        elif opcao == 3:
            mostrar_cardapio()
            escolha = int(input("Escolha o lanche pelo número: "))
            fazer_pedido(escolha)
            mensagem("Pedido realizado!")
        elif opcao == 4:
            mensagem(f"O total é R${calcular_total()}")
        elif opcao == 5:
            mensagem("Saindo...")
            break
        else:
            mensagem("Opção inválida.")
        
main()
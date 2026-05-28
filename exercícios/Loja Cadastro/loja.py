lista_produtos = []
valor_produtos = []
carrinho = []
valor_total = 0

def cadastrar_produtos():
    nome_produto = input("\nInforme o nome do produto: ")
    valor_produto = int(input("Informe o valor do produto: "))

    lista_produtos.append(nome_produto)
    valor_produtos.append(valor_produto)

    mensagem = print(f"Nome: {nome_produto}\nValor: {valor_produto}\n[Produto cadastrado com sucesso!]")
    return mensagem

def menu():
    print(" --- Menu de Produtos --- ")
    for i in range(len(lista_produtos)):
        print(f"{i} - {lista_produtos[i]} - R$ {valor_produtos[i]}")

def calcular_desconto():
    global valor_total
    if valor_total > 100:
        desconto = valor_total * 0.1
        valor_total -= desconto
        print(f"\nDesconto aplicado! Novo valor: {valor_total}")
    else:
        print("\nO desconto é aplicado somente em compras a cima de R$ 100,00")

def comprar():
    global valor_total # para conseguir alterar o valor
    while True:
        menu()
        produto_compra = int(input("Informe o número do produto que deseja comprar: "))

        if produto_compra >= len(lista_produtos):

            print("Produto inexistente. Tente Novamente!")
            
        else:
            carrinho.append(f"{lista_produtos[produto_compra]}")

            valor_total += valor_produtos[produto_compra]

            print("\n[Produto adicionado ao carrinho]")

            opcao = input("Deseja comprar outro produto? [sim] [nao]: ")

            if opcao in ['sim', 's']:
                continue

            elif opcao in ['nao', 'n']:
                break
            else:
                print("[Opção inválida!]")

def ver_carrinho():
    print(f"{20*'-'}\nProdutos do seu carrinho:")
    for i in range(len(carrinho)):
        print(f"{i+1} - {carrinho[i]}")
    print(f"{20*'-'}")

def calcular_total():
    global valor_total
    if valor_total > 100:
        desconto = valor_total * 0.1
        valor_total = valor_total - desconto
        print(f"\nValor total a pagar: R$ {valor_total} (Desconto aplicado)")
    else:
        print(f"\nValor total a pagar: R$ {valor_total}")

def main():
    while True:
        try:
            print("--- Loja do Python ---\n")
            op = int(input("Escolha uma opção:\n[1] - Cadastrar Produtos\n[2] - Comprar produtos\n[3] - Calcular Desconto\n[4] - Calcular Total\n[5] - Ver Carrinho\n[6] - Sair\n-> "))
            if op == 1:
                cadastrar_produtos()
            elif op == 2:
                comprar()
            elif op == 3:
                calcular_desconto()
            elif op == 4:
                calcular_total()
            elif op == 5:
                ver_carrinho()
            elif op == 6:
                print("\nSaindo...")
                break
            else:
                print("\n[Opção Inválida! Tente novamente.]")
        except ValueError():
            print("\n[Operação Inválida]")

main()
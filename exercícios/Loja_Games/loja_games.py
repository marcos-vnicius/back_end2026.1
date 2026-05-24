""" LOJA DE GAMES """

lista_jogos = ["Minecraft", "GTA V", "FIFA"]
preco_jogos = [80, 120, 90]
total_compra = []
valor_total = 0

while True:
    try:
        print("----- LOJA DE GAMES DO PYTHON -----")
        opcao = int(input("Escolha uma opção:\n[1- Comprar] [2 - Mostrar Total] [3 - Sair]\n -> "))
        
        # ----- OPÇÃO 1
        if opcao == 1:
            print("----- Lista de Jogos -----")
            for i in range(len(lista_jogos)):
                print(f"{i+1} - {lista_jogos[i]} - R$ {preco_jogos[i]}\n{20*"-"}")
            compra = int(input("Qual jogo deseja comprar? [1] [2] [3]\n-> "))
            
            if compra == 1:
                total_compra.append(lista_jogos[0])
                valor_total += preco_jogos[0]
                print(f"Compra realizada com sucesso!\n{20*"-"}")
            
            elif compra == 2:
                total_compra.append(lista_jogos[1])
                valor_total += preco_jogos[1]
                print(f"Compra realizada com sucesso!\n{20*"-"}")
                

            elif compra == 3:
                total_compra.append(lista_jogos[2])
                valor_total += preco_jogos[2]
                print(f"Compra realizada com sucesso!\n{20*"-"}")

            else:
                print("[Operação inválida]")
            

        # ----- OPÇÃO 2
        elif opcao == 2:
            print("\n--- Total da Compra ---")
            for i in range(len(total_compra)):
                print(f"{i+1} - {total_compra[i]} - R$ {preco_jogos[i]}")
            if valor_total > 200:
                desconto10p = valor_total * 0.1
                valor_total -= desconto10p
                print(f"\nDesconto de 10% aplicado!\nValor Total: R$ {valor_total}")
            else:
                print(f"\nTotal da compra: R$ {valor_total}")
            print(20*"-")

        # ----- OPÇÃO 3
        elif opcao == 3:
            print("\n[Programa Encerrado]")
            break
        else:
            print("\n[Opção Inválida, tente novamente]")

    except ValueError:
        print("\n[Operação inválida]")
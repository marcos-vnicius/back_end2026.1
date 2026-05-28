filmes_cartaz = []
valor_ingressos = []

ingressos_vendidos = []
valor_ingressos_vendidos = []


def mensagem(msg):
    print(msg)


def cadastrar_filme():
    while True:
        try:
            filme_cadastro = input("\nInforme o nome do filme: ")
            valor_cadastro = int(input("Informe o valor do ingresso: "))

            filmes_cartaz.append(filme_cadastro)
            valor_ingressos.append(valor_cadastro)

            mensagem("\n[Cadastro realizado com sucesso]")
            while True:
                opcao = input("Deseja fazer outro cadastro?: ").lower()

                if opcao in ['sim', 's']:
                    break

                elif opcao in ['nao', 'não', 'n']:
                    return
                
                else:
                    mensagem("[Opção Inválida]")
                    
        except ValueError:
            mensagem("[Operação inválida]")


def menu_filmes():
    mensagem("\n--- FILMES EM CARTAZ ---")

    for i in range(len(filmes_cartaz)):
        mensagem(f"{i+1} - Filme: {filmes_cartaz[i]} - Ingresso: R$ {valor_ingressos[i]}\n{20*"-"}")


def comprar():
    while True:
        try:
            menu_filmes()
            
            filme_compra = int(input("Informe o número do filme que deseja comprar: "))

            if filme_compra > len(filmes_cartaz):
                mensagem("[Opção inválida! Tente novamente.]")
                return
            
            else:
                ingressos_vendidos.append(filmes_cartaz[filme_compra - 1])
                valor_ingressos_vendidos.append(valor_ingressos[filme_compra - 1])

                mensagem("[Compra realizada com sucesso!]")

                while True:
                    opc = input("Deseja realizar outra compra?: ")
                    if opc in ['sim', 's']:
                        break
                    elif opc in ['nao', 'não', 'n']:
                        return
                    else:
                        mensagem("[Opção inválida! Tente novamente.]")
                        
        except ValueError:
            mensagem("[Operação inválida]")

def mostrar_vendas():
    mensagem("\n--- INGRESSOS VENDIDOS ---")
    for i in range(len(ingressos_vendidos)):
        mensagem(f"{i+1} - {ingressos_vendidos[i]} - R$ {valor_ingressos_vendidos[i]}")
        mensagem(f"[ Foram vendidos [{len(ingressos_vendidos)}] ingressos e R$ {valor_ingressos_vendidos} arrecadado ao total ]")
    mensagem(20*"-")


def main():
    while True:
        try:
            mensagem("\n----- Cinema Python -----")
            opcao_inicio = int(input("Informe o número da opção desejada:\n[1] - Cadastrar Filmes\n[2] - Comprar Ingressos\n[3] - Mostrar Vendas e Arrecadação\n[4] - Sair \n-> "))
           
            if opcao_inicio == 1:
                cadastrar_filme()
            elif opcao_inicio == 2:
                comprar()
            elif opcao_inicio == 3:
                mostrar_vendas()
            elif opcao_inicio == 4:
                mensagem("\nSaindo...")
                break
            else:
                mensagem("[Opção inválida! Tente novamente]")

        except ValueError:
            mensagem("[Operação Inválida]")

main()
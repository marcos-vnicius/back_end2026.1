def mensagem(msg):
    print(msg)

class Jogo():
    def __init__(self, nome_jogo, categoria_jogo, preco_jogo):
        self.nome = nome_jogo
        self.categoria = categoria_jogo
        self.preco = preco_jogo

    def mostrar_dados(self):
        mensagem(f"Nome do Jogo: {self.nome}\nCategoria: {self.categoria}\nPreço: {self.preco}\n{20*"-"}")


class Loja():
    def __init__(self):
        self.lista_jogos = []
    
    def cadastrar_jogos(self):
        while True:
            try:
                jogo_cadastro = input("\nInforme o nome do jogo: ")
                categoria_cadastro = input("Informe a categoria do jogo: ")
                preco_cadastro = int(input("Informe o preço do jogo: "))
                
                jogo = Jogo(jogo_cadastro, categoria_cadastro, preco_cadastro)
                self.lista_jogos.append(jogo)
                mensagem("[Jogo cadastrado com sucesso!]")

                while True:
                    op = input("\nDeseja fazer outro cadastro? [sim] [nao]: ")
                    if op in ['sim', 's']:
                        break
                    elif op in ['não', 'nao', 'n']:
                        return
                    else:
                        mensagem("[Opção inválida]")

            except ValueError:
                mensagem("[Operação Inválida]")
    
    def mostrar_jogos(self):
        mensagem("\n----- Jogos Disponíveis -----")
        for jogo in self.lista_jogos:
            jogo.mostrar_dados()
    
    def compra(self):
        while True:
            self.mostrar_jogos()
            jogo_compra = int(input("Informe o número do jogo que deseja comprar: "))
            if jogo_compra > len(self.lista_jogos):
                mensagem("[Opção indisponível]")
                break
            else:
                mensagem("[Compra realizada com sucesso!]")
                return
            
    def main(self):
        while True:
            try:
                mensagem("\n---- Loja Games do Python ----")
                opcao = int(input("Informe o número da opção desejada:\n[1] - Cadastrar Jogos\n[2] - Jogos Disponíveis\n[3] - Comprar Jogos\n[4] - Sair\n-> "))
                if opcao == 1:
                    self.cadastrar_jogos()
                elif opcao == 2:
                    self.mostrar_jogos()
                elif opcao == 3:
                    self.compra()
                elif opcao == 4:
                    mensagem("Saindo...")
                    break
            except ValueError:
                mensagem("[Operação Inválida]")

loja = Loja()
loja.main()
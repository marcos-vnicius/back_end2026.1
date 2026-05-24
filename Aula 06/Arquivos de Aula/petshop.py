#Instância a clase Animal dentro da classe PetShop
#Herança é uma ligação (petshop ao animal)

class Animal():
    def __init__(self, nome, tipo, idade):
        self.nome_animal = nome
        self.tipo_animal = tipo
        self.idade_animal = idade

    def mostrar_dados(self):
        mensagem = f"{20*"-"}\nNome: {self.nome_animal}\nTipo: {self.tipo_animal}\nIdade: {self.idade_animal}\n{20*"-"}"
        return mensagem
    
 # Cria a classe PetShop()
class PetShop():
    def __init__(self):
        self.animais = [] #lista

    def cadastrar_animais(self):
         # guarda as características do animal
        cad_nome = input("\nInforme o nome do animal: ")
        cad_tipo = input("Informe o tipo do animal: ")
        cad_idade = input("Informe a idade do animal: ")

         # variável que receberá a classe Animal() com as informações necessárias (cad_nome, cad_tipo, cad_idade)
        meu_animal = Animal(cad_nome, cad_tipo, cad_idade) # Herança

         # adicionar animal à lista de animais
        self.animais.append(meu_animal)

         # retorna a mensagem de confirmação de cadastro
        print("[ Animal cadastrado com sucesso! ]\n")
    
    def mostrar_animais(self):
         # mostra a apresentação da função chamada
        print("\n----- ANIMAIS CADASTRADOS -----")
        
         # lista os animais cadastrados conforme a função mostrar_dados()
        for meu_animal in self.animais:
            print(meu_animal.mostrar_dados())

     # Cria o método de execução do programa (onde a mágica acontece)
    def main(self):
        while True:
            try:
                opcao = int(input("Escolha uma opção:\n[1 - Cadastrar Animais]\n[2 - Mostrar Animais]\n[3 - Sair]\n    -> "))
                if opcao == 1:
                    self.cadastrar_animais()
                elif opcao == 2:
                    self.mostrar_animais()
                elif opcao == 3:
                    break
                else:
                    mensagem = "[Opção inválida! Por favor, tente novamente]"
                    return mensagem
            except ValueError:
                mensagem = "[Operação inválida! Por favor, tente novamente]"
                return mensagem

 # cria a variável que recebera as funcionalidades da classe PetShop()
loja = PetShop()

 # executa o programa
loja.main()
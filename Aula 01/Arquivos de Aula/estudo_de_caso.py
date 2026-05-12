jogos = ["Minecraft", "GTA V", "FIFA", "The Sims"]
valor_minecraft = 80
valor_gtav = 120
valor_fifa = 90
valor_thesims = 70
valor_total = 0
desconto = valor_total * 0.1
carrinho = []


print("--- LOJA DE GAMES ---")
print("Jogos disponíveis:")
for i in jogos:
    print("- " + i)

resp_compra = input("Deseja fazer uma compra? ").lower()
while resp_compra in ["sim", "s", "desejo", "positivo"]:
    compra = input("Qual jogo você deseja comprar? ").lower()
    if compra == "minecraft":
        valor_total += valor_minecraft
        carrinho.append("Minecraft")
        print("Jogo adicionado ao carrinho")
    elif compra in ["gtav", "gta v", "gta"]:
        valor_total += valor_gtav
        carrinho.append("GTA V")
        print("Jogo adicionado ao carrinho")
    elif compra == "fifa":
        valor_total += valor_fifa
        carrinho.append("FIFA")
        print("Jogo adicionado ao carrinho")
    elif compra in ["the sims", "thesims", "sims"]:
        valor_total += valor_thesims
        carrinho.append("The Sims")
        print("Jogo adicionado ao carrinho")
    print("---------")
    print(f"Jogos no carrinho:")
    for i in carrinho:
        print(f"- {i}")
    

    resp_compra = input("Deseja comprar mais um jogo? ")
    
    
    if resp_compra in ["sim", "s", "desejo", "positivo"]:
        continue
    elif resp_compra in ["não", "nao", "n", "negativo"]:
        break
    else:
        print("Resposta inválida")
        continue
if valor_total > 200:
    valor_total -= desconto
    print("Desconto aplicado!")
print(f"Valor total da compra: R$ {valor_total}")

""" CORRIGIDO """

""" Estudo de Caso: Loja de Games """
 
""" #Declarar as listas
jogos = ["Minecraft", "GTA V", "FIFA", "PAC MAN"]
precos = [80, 120, 90, 50]
 
total = 0
 
#Exibe menu para escolha
for i in range(len(jogos)):
    print(i, "-", jogos[i],"- R$", precos[i] )
 
#Usuario seleciona
for i in jogos:
    escolha = int(input("Escolha o jogo: [0] [1] [2] [3]: "))
    total += precos[escolha]
 
    seguir = input("Deseja escolher outro jogo? [s] [n]").lower()
 
    if seguir in ["s", "sim"]:
        continue
    else:
        break
 
if total > 200:
    desconto = total * 0.10
    total -= desconto
    print("Desconto aplicado!")
 
print(f"Total Final: R${total:.2f}") """
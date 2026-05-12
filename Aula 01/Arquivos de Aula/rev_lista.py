""" Crie uma lista que guarde as
    armas do jogo """

""" Lista (Array) """
inventario = ["Espada", "Poção", "Escudo"]

print("Inventario 01")
for i in inventario:
    print(i)

inventario.append("Lança")
print("Inventario 02")
for i in inventario:
    print(i)


""" Tupla é imutável, não da pra modificar """

valor_ataque = (10, 20)

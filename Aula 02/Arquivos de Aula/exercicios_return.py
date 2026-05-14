def multiplicar(n1, n2):
    return n1 * n2

def media(n1, n2):
    return (n1 + n2) / 2

def desconto_10(valor_compra):
    desconto = valor_compra * 0.10
    return valor_compra - desconto
    
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

print(multiplicar(num1, num2))
print(media(num1, num2))

valor = int(input("Informe o valor da compra: "))
valor_desconto = desconto_10(valor)
print(f"Desconto aplicado! Novo valor a pagar: {valor_desconto}")
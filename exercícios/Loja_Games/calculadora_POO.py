class Calculadora():
    def __init__(self, num_1, num_2):
        self.number_1 = num_1
        self.number_2 = num_2
    
    def somar(self):
        resultado = f"O resultado da dvisão é igual a {self.number_1 + self.number_2}"
        return resultado
    
    def subtrair(self):
        resultado = f"O resultado da dvisão é igual a {self.number_1 - self.number_2}"
        return resultado
    
    def multiplicar(self):
        resultado = f"O resultado da dvisão é igual a {self.number_1 * self.number_2}"
        return resultado
    
    def dividir(self):
        if self.number_2 == 0:
            resultado = "[Não é possível divisão por zero]"
            return resultado
        else:
            resultado = f"O resultado da dvisão é igual a {self.number_1 / self.number_2}"
            return resultado
    
def main():
    while True:
        try:
            print("----- CALCULADORA PYTHON -----\n")
            primeiro_valor = int(input("Informe o primeiro valor: "))
            segundo_valor = int(input("Informe o segundo valor: "))
            opcao = int(input("\nEscolha uma opção:\n [1 - Somar] [2 - Subtrair] [3 - Multiplicar] [4 - Dividir]\n -> "))
            calculadora_python = Calculadora(primeiro_valor, segundo_valor)

            if opcao == 1:
                print(f"\n{calculadora_python.somar()}")
                
            elif opcao == 2:
                print(f"\n{calculadora_python.subtrair()}")
                
            elif opcao == 3:
                print(f"\n{calculadora_python.multiplicar()}")
                
            elif opcao == 4:
                print(f"\n{calculadora_python.dividir()}")

            else:
                print(f"\n[Operação Inválida]")
            
            opcao_2 = input("Fazer outra operação? [1 - Sim] ou [Qualquer tecla para encerrar] -> ")
            if opcao_2 in ["1", "sim", "s"]:
                continue
            else:
                print("[Programa Encerrado]\n")
                break

            
        except ValueError:
            print("\n[Operação Inválida]")
            continue
            
main()
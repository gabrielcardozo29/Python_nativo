#CALCULADORA SIMPLES DE 2 VALORES, COM 4 OPERAÇÕES BÁSICAS PARA PRÁTICA DE FUNÇÃO.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b == 0:
        return "Erro, divisão por 0"
    return a / b
#________________________________________________________________________________

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print()
print("[1] - somar\n[2] - subtrair\n[3] - Multiplicar\n[4] - dividir")
print()
op = input("Escolha uma operação:")

def exibir_resultado(a, b, oprerador, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} {oprerador} {b} é {resultado}")

if op == "1":
   exibir_resultado(a, b, "+", somar)
    
elif op == "2":
    exibir_resultado(a, b, "-", subtrair)
    
elif op == "3":
    exibir_resultado(a, b, "*", multiplicar)
    
elif op == "4":
    exibir_resultado(a, b, "/", dividir)
else:
    resultado = "Opção inválida"


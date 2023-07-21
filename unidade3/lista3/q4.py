#Faça um programa que leia dois números n1 e n2, onde 1 <= n1 <= n2 <= 10, e que imprima a tabuada dos números entre n1 e n2, conforme exemplo.
def imprimir_tabuada(n1, n2):
    for i in range(n1, n2 + 1):
        print(f"Tabuada do {i}:")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
            
n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))

if n1 < 1 or n2 > 10 or n1 > n2:
    print("Valores inválidos. Certifique-se de que 1 <= n1 <= n2 <= 10.")
else:
    imprimir_tabuada(n1, n2)

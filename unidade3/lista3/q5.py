#Crie um programa que leia um número N (0 < N < 10) e que imprima uma sequência de números conforme mostrado no exemplo:
def imprimir_sequencia(n):
    for i in range(1, n+1):
        numero = str(i) * i
        print(numero)

N = int(input("Digite um valor entre 0 e 10: "))

if N <= 0 or N >= 10:
    print("Valor inválido. Certifique-se de que 0 < N < 10.")
else:
    imprimir_sequencia(N)

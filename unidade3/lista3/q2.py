#Escreva um programa que receba um número N para gerar os N primeiros termos da série de Fibonacci: 1, 1, 2, 3, 5, 8, 13, …
def fibonacci(n):
    sequence = [1, 1] 
    for i in range(2, n):
        termo_atual = sequence[i - 1] + sequence[i - 2]
        sequence.append(termo_atual)

    return sequence

N = int(input("Digite o valor de N: "))

sequencia_fibonacci = fibonacci(N)

for termo in sequencia_fibonacci:
    print(termo, end=" ")

#Escreva um programa que peça ao usuário dois números inteiros n1 e n2 (n2 > n1) e imprima quantos números primos existem no intervalo [n1, n2], incluindo esses dois números. Lembre-se que um número é primo se ele é divisível apenas por 1 e por ele mesmo.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2 (maior que n1): "))

count = 0
for num in range(n1, n2 + 1):
    if is_prime(num):
        count += 1

print("Existem", count, "números primos no intervalo entre", n1, "e", n2, "")


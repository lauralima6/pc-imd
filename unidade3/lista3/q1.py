#Crie um programa que leia dois números positivos n1 e n2, ambos maiores que 1, e que imprima os números ímpares não primos entre esses dois números, incluindo os próprios n1 e n2. Não assuma que n1 < n2. Se for ao contrário, troque os valores de n1 com n2.
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_impares_nao_primos(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1

    for numero in range(n1, n2 + 1):
        if numero % 2 != 0 and not eh_primo(numero):
            print(numero)
            
n1 = int(input("Digite o primeiro número (maior que 1): "))
n2 = int(input("Digite o segundo número (maior que 1): "))

imprimir_impares_nao_primos(n1, n2)

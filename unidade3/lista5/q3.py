#Escreva um programa que peça ao usuário um número inteiro N e depois um conjunto de N números. O programa deverá armazenar todos os números lidos numa lista, e então imprimir todos os números, classificando se cada número é primo ou não, no caso se não ser primo o programa também deve imprimir a lista de divisores do número.
#Para verificar se um número é primo ou não, escreva uma função que recebe um número inteiro como parâmetro e retorna à sua lista de divisores. Use o retorno da função para imprimir a saída do programa no formato abaixo:
def verificar_primo(numero):
    divisores = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def imprimir_numeros_primos_e_divisores(lista_numeros):
    for numero in lista_numeros:
        divisores = verificar_primo(numero)
        if len(divisores) == 2:
            print(f'O número {numero} é primo.')
        else:
            print(f'O número {numero} não é primo. Divisores: {divisores}')

n = int(input('Digite a quantidade de números: '))

numeros = []
for i in range(n):
    numero = int(input(f'Digite o número {i+1}: '))
    numeros.append(numero)

imprimir_numeros_primos_e_divisores(numeros)

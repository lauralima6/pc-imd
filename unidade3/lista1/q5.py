#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1 - o produto do dobro do primeiro com metade do segundo .
#2 - a soma do triplo do primeiro com o terceiro.
#3 - o terceiro elevado ao cubo.
def calcula_operacoes(num_inteiro1, num_inteiro2, num_real):
    resultado1 = (2 * num_inteiro1) * (num_inteiro2 / 2)
    
    resultado2 = (3 * num_inteiro1) + num_real

    resultado3 = num_real ** 3

    print("Resultados:")
    print(f"Produto do dobro do primeiro com metade do segundo: {resultado1}")
    print(f"Soma do triplo do primeiro com o terceiro: {resultado2}")
    print(f"Terceiro elevado ao cubo: {resultado3}")

num_inteiro1 = int(input("Digite o primeiro número inteiro: "))
num_inteiro2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite o número real: "))

calcula_operacoes(num_inteiro1, num_inteiro2, num_real)

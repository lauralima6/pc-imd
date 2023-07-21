#Um número inteiro positivo,n, é dito triangular se, e somente se, ele é o resultado do produto de três números inteiros positivos e consecutivos. Escreva um algoritmo que leia um número inteiro positivo, n, e escreva como saída “é triangular” se n for triangular e “não é triangular”, caso contrário.
def verificar_triangular(numero):
    i = 1
    while i * (i + 1) * (i + 2) < numero:
        i += 1

    if i * (i + 1) * (i + 2) == numero:
        return True
    else:
        return False


n = int(input("Digite um número inteiro positivo: "))


if verificar_triangular(n):
    print("É triangular")
else:
    print("Não é triangular")

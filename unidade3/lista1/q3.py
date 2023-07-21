#Escreva um programa que recebe do usuário dois textos, A e B, e imprime os resultados das operações tamanho(A) - tamanho(B), A + B, A contém B, B contém A, primeira letra de A, primeira letra de B, última letra de A, última letra de B.
def operacoes_texto(A, B):
    resultado_tamanho = len(A) - len(B)

    resultado_concatenacao = A + B

    resultado_contem_b = B in A

    resultado_contem_a = A in B

    primeira_letra_a = A[0] if len(A) > 0 else None

    primeira_letra_b = B[0] if len(B) > 0 else None

    ultima_letra_a = A[-1] if len(A) > 0 else None

    ultima_letra_b = B[-1] if len(B) > 0 else None

    print("Resultados:")
    print(f"Tamanho(A) - Tamanho(B) = {resultado_tamanho}")
    print(f"A + B = {resultado_concatenacao}")
    print(f"A contém B? {resultado_contem_b}")
    print(f"B contém A? {resultado_contem_a}")
    print(f"Primeira letra de A: {primeira_letra_a}")
    print(f"Primeira letra de B: {primeira_letra_b}")
    print(f"Última letra de A: {ultima_letra_a}")
    print(f"Última letra de B: {ultima_letra_b}")


A = input("Digite o texto A: ")
B = input("Digite o texto B: ")
operacoes_texto(A, B)

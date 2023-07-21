#Escreva um programa que recebe dois textos do usuário e imprime o valor das expressões de acordo com os exemplos:
#1 - Texto A dividido em duas Partes: primeira_metade_texto(A) e segunda_metade_texto(A)
#2 - Texto B dividido em duas Partes: primeira_metade_texto(B) e segunda_metade_texto(B)
#3 - primeira_metade_texto(A) + segunda_metade_texto(B)
#4 - segunda_metade_texto(A) + primeira_metade_texto(B)
#5 - primeira_letra_texto(A) + segunda_letra_texto(B) + ultima_letra_texto(A) + ultima_letra_texto(B)
def primeira_metade_texto(texto):
    metade = len(texto) // 2
    return texto[:metade]

def segunda_metade_texto(texto):
    metade = len(texto) // 2
    return texto[metade:]

def primeira_letra_texto(texto):
    return texto[0] if len(texto) > 0 else None

def segunda_letra_texto(texto):
    return texto[1] if len(texto) > 1 else None

def ultima_letra_texto(texto):
    return texto[-1] if len(texto) > 0 else None

textoA = input("Digite o texto A: ")
textoB = input("Digite o texto B: ")

primeira_metade_A = primeira_metade_texto(textoA)
segunda_metade_A = segunda_metade_texto(textoA)
primeira_metade_B = primeira_metade_texto(textoB)
segunda_metade_B = segunda_metade_texto(textoB)
expressao_3 = primeira_metade_A + segunda_metade_B
expressao_4 = segunda_metade_A + primeira_metade_B
expressao_5 = (
    primeira_letra_texto(textoA)
    + segunda_letra_texto(textoB)
    + ultima_letra_texto(textoA)
    + ultima_letra_texto(textoB)
)

print("Resultados:")
print(f"Texto A dividido em duas partes: {primeira_metade_A} + {segunda_metade_A}")
print(f"Texto B dividido em duas partes: {primeira_metade_B} + {segunda_metade_B}")
print(f"primeira_metade_texto(A) + segunda_metade_texto(B) = {expressao_3}")
print(f"segunda_metade_texto(A) + primeira_metade_texto(B) = {expressao_4}")
print(f"primeira_letra_texto(A) + segunda_letra_texto(B) + ultima_letra_texto(A) + ultima_letra_texto(B) = {expressao_5}")


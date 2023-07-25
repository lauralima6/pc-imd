# Escreva uma função que receba uma lista de números inteiros e um valor inteiro como entrada, e retorne a posição do valor na lista. Se o valor não estiver na lista, retorne -1.

def encontrar_posicao(lista, valor):
    for i, num in enumerate(lista):
        if num == valor:
            return i
    return -1
    
def gerar_lista_do_usuario():
    lista = []
# o código pede os valores da lista ao usuário até que a quantidade de elementos seja igual a 6
    while True:
        valor = input("Entrada: ")
        lista.append(valor)
        if len(lista) == 6:
            break  
    return lista
    
lista_gerada = gerar_lista_do_usuario()
print("Lista gerada:", lista_gerada)

valor1 = input("Valor: ")
posicao = encontrar_posicao(lista_gerada, valor1)
print(f"Saída: {posicao}")




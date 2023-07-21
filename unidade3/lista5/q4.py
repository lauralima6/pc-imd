#Implemente uma função semelhante ao split(), porém sobre listas numéricas. Sua função deve se chamar imprimePartes e receber dois parâmetros, a lista e o elemento separador. A função então deve imprimir as listas geradas durante o processo de quebra. Caso haja mais de uma ocorrência consecutiva do elemento separador, não devem ser geradas listas vazias. Por exemplo, na quebra da sequência [ 2, 7, 3, 3, 3, 3, 3, 4, 8, 5 ] pelo valor 3, apenas as sequências [ 2, 7 ] e [ 4, 8, 5 ] são geradas. O mesmo vale no caso do elemento separador se encontrar no início ou no final da sequência. Por exemplo, a quebra de [ 3, 3, 3, 4, 8, 5, 3, 3 ] irá gerar apenas a sequência [ 4, 8, 5 ].
#Escreva então um programa que lê do usuário um valor N, uma sequência numérica com N valores e o valor do separador. Use a função imprimePartes, para imprimir as partes resultantes da separação.

def imprimePartes(lista, separador):
    partes = []
    parte_atual = []
    
    for elemento in lista:
        if elemento == separador:
            if parte_atual:
                partes.append(parte_atual)
                parte_atual = []
        else:
            parte_atual.append(elemento)
    
    if parte_atual:
        partes.append(parte_atual)
    
    for parte in partes:
        print(parte)

n = int(input("Digite a quantidade de valores: "))

sequencia = []
for i in range(n):
    valor = int(input(f"Digite o valor {i+1}: "))
    sequencia.append(valor)

separador = int(input("Digite o valor do separador: "))

if len(set(sequencia)) == 1:
  print("Nenhuma sequência resultante")
else:
  print("Sequências resultantes: ")

imprimePartes(sequencia, separador)

#Escreva um programa que pede ao usuário um texto e dois números inteiros i1 e i2. Após lidas as entradas o programa faz as seguintes verificações:
#Se i1 > i2 troque os valores de i1 e i2
#Se i1 ou i2 forem maiores ou iguais ao tamanho do texto lido, finalize o programa avisando ao usuário que os valores tem que ser menores do que o tamanho do texto.
#Após feitas as verificações, o programa deverá imprimir partes do texto conforme as especificações abaixo:
#Parte 1: equivale à parte do texto que vai da primeira letra até o índice i1
#Parte 2: equivale à parte do texto que vai da primeira letra até o índice i2
#Parte 3: equivale à parte do texto que vai da letra de índice i1 letra até o índice i2
#Parte 4: equivale à parte do texto que vai da letra de índice i1 até o final do texto
#Parte 5: equivale à parte do texto que vai da letra de índice i2 até o final do texto
texto = input("Digite um texto: ")
i1 = int(input("Digite o primeiro número inteiro (i1): "))
i2 = int(input("Digite o segundo número inteiro (i2): "))

if i1 > i2:
    i1, i2 = i2, i1

if i1 >= len(texto) or i2 >= len(texto):
    print("Os valores de i1 e i2 devem ser menores do que o tamanho do texto.")
else:
    parte1 = texto[:i1]
    parte2 = texto[:i2]
    parte3 = texto[i1:i2]
    parte4 = texto[i1:]
    parte5 = texto[i2:]

    print("Parte 1:", parte1)
    print("Parte 2:", parte2)
    print("Parte 3:", parte3)
    print("Parte 4:", parte4)
    print("Parte 5:", parte5)

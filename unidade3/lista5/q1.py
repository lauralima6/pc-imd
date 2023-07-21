#Escreva um programa que faça a criptografia de uma palavra, da seguinte forma:
#Letras de "a" até "e" - 1
#Letras de "f" até "j" - 2
#Letras de "k" até "o" - 3
#Letras de "p" até "z" - 4
#Espaço ou qualquer outro caracter - 5
#O programa deve ter uma função que recebe, como parâmetro de entrada, uma palavra e retorne o valor encriptado correspondente. Seu programa deve realizar a leitura do texto fora da função e usá-la bem como seu retorno para imprimir a saída como os exemplos mostram.

def criptografar(palavra):
    palavra = palavra.lower() 
    criptografada = ""

    for letra in palavra:
        if letra >= 'a' and letra <= 'e':
            criptografada += '1'
        elif letra >= 'f' and letra <= 'j':
            criptografada += '2'
        elif letra >= 'k' and letra <= 'o':
            criptografada += '3'
        elif letra >= 'p' and letra <= 'z':
            criptografada += '4'
        else:
            criptografada += '5'

    return criptografada

palavra = input("Digite uma palavra: ")

resultado = criptografar(palavra)
print("Palavra criptografada:", resultado)

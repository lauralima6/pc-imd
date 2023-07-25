# Crie um jogo em que o programa "pense" em um número aleatório e o usuário tenha que adivinhar esse número. O programa deve dar dicas se o número fornecido pelo usuário é maior ou menor que o número pensado, até que o usuário acerte.

import random

def jogo_adivinhacao():
  
    numero_minimo = 1
    numero_maximo = 100

    numero_pensado = random.randint(numero_minimo, numero_maximo)

    print(f"Eu pensei em um número entre {numero_minimo} e {numero_maximo}.")

    tentativas = 0
    while True:
        tentativa = int(input("Tente adivinhar qual é o número: "))
        tentativas += 1

        if tentativa < numero_pensado:
            print("Tente um número maior!")
        elif tentativa > numero_pensado:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou! O número era {numero_pensado}.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()

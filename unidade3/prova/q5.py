# Crie uma função que receba um número inteiro como entrada e retorne os dois números primos gêmeos (números primos cuja diferença é igual a 2) que são maiores que o número fornecido.
def is_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

def encontrar_primos_gemeos_maiores_que(numero):
    primos_gemeos = []
    numero2 = numero + 1

    while len(primos_gemeos) < 2:
        if is_primo(numero2):
            if len(primos_gemeos) == 0 or numero2 - primos_gemeos[-1] == 2:
                primos_gemeos.append(numero2)
        numero2 += 1

    return tuple(primos_gemeos)

numero = int(input("Entrada: "))
resultado = encontrar_primos_gemeos_maiores_que(numero)
print(f"Saída: {resultado}")

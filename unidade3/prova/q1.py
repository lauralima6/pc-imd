# Desenvolva um programa que peça ao usuário uma palavra e verifique se ela é um palíndromo. Um palíndromo é uma palavra que é lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.
# Exemplos:
# Digite a palavra: radar A palavra "radar" é um palíndromo.
# Digite a palavra: python A palavra "python" NÃO é um palíndromo.

def is_palindrome(palavra):
    palavra = palavra.replace(" ", "").lower()
    
   
    return palavra == palavra[::-1]

def main():
    user_input = input("Digite a palavra: ")
    
    if is_palindrome(user_input):
        print(f'A palavra "{user_input}" é um palíndromo.')
    else:
        print(f'A palavra "{user_input}" NÃO é um palíndromo.')

if __name__ == "__main__":
    main()

# Crie programa que contenha uma função que receba duas strings como entrada e determine se elas são anagramas. Ou seja, se uma é a permutação dos caracteres da outra.
# Exemplos:
# Entrada: str1 = "amor" str2 = "roma" Saída: As palavras "amor" e "roma" são anagramas.
# Entrada: str1 = "arara" str2 = "ararea" Saída: As palavras "arara" e "ararea" NÃO são anagramas.

def sao_anagramas(str1, str2):
  
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if len(str1) != len(str2):
        return False

    count_str1 = {}
    count_str2 = {}
    
    for char in str1:
        count_str1[char] = count_str1.get(char, 0) + 1

    for char in str2:
        count_str2[char] = count_str2.get(char, 0) + 1

    return count_str1 == count_str2

def main():
    str1 = input("Digite a primeira palavra: ")
    str2 = input("Digite a segunda palavra: ")

    if sao_anagramas(str1, str2):
        print(f'As palavras "{str1}" e "{str2}" são anagramas.')
    else:
        print(f'As palavras "{str1}" e "{str2}" NÃO são anagramas.')

if __name__ == "__main__":
    main()

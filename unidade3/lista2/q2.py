#A ordem lexicográfica é a ordem das palavras usada em um dicionário, por exemplo, o verbo "ser" vem antes da palavra "seres", na ordem lexicográfica. Embora possa parecer que tem algo a ver com o tamanho da palavra, a palavra "testando" viria antes da palavra "testes" na ordem lexicográfica.
#Na linguagem python, podemos testar se uma plavra vem antes da outra de acordo com a ordem lexicográfica usando os operadores ">" ou "<". Dessa forma sejam as palavras A e B, se A < B, a vem antes de B; de forma análoga, se A > B, B vem antes de A. Obs: para comparações da ordem lexicográfica, considere os textos todos minúsculos!
#Assim escreva um programa que lê três textos do usuário e os imprime na ordem lexicográfica de acordo com os exemplos abaixo:
texto1 = input("Digite o primeiro texto: ").lower()
texto2 = input("Digite o segundo texto: ").lower()
texto3 = input("Digite o terceiro texto: ").lower()

textos = [texto1, texto2, texto3]

textos_ordenados = sorted(textos)

print("Textos em ordem lexicográfica:")
for texto in textos_ordenados:
    print(texto)

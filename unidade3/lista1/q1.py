#Escreva um programa que pede ao usuário 2 números decimais (float) A e B, e imprime o resultado das operações de adição, subtração, divisão, divisão inteira e resto entre A e B. No caso de operações entre números inteiros, como resto e divisão inteira, converta os números em inteiro antes de realizar as operações.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
divisao_inteira = int(n1) // int(n2)
divisao_resto = int(n1) % int(n2)
print('A soma entre {} e {} é igual a {:.2f}'.format(n1,n2,soma))
print('A subtracao entre {} e {} é igual a {:.2f}'.format(n1,n2,subtracao))
print('A divisão entre {} e {} é igual a {:.2f}'.format(n1,n2,divisao))
print('A divisão inteira entre {} e {} é igual a {}'.format(int(n1),int(n2),divisao_inteira))
print('A divisão com resto entre {} e {} é igual a {}'.format(int(n1),int(n2),divisao_resto))
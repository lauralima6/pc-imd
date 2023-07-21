#Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada aluno e imprimi-los na ordem inversa.

N = int(input("Digite o valor de N: "))

numeros = []

for i in range(N):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)
OP = int(input("Digite o número da operação (0 para soma, 1 para multiplicação): "))
if OP != 0 and OP != 1:
    print("Operação inválida. Digite 0 para soma ou 1 para multiplicação.")
    exit()
    
A = int(input("Digite a posição A na lista (de 1 a N): ")) - 1 
B = int(input("Digite a posição B na lista (de 1 a N): ")) - 1 

if OP == 0:
    resultado = numeros[A] + numeros[B]
    operacao = "soma"
    print(f"Resultado: {numeros[A]} + {numeros[B]} = {resultado}")
elif OP == 1:
    resultado = numeros[A] * numeros[B]
    operacao = "multiplicação"
    print(f"Resultado: {numeros[A]} * {numeros[B]} = {resultado}")




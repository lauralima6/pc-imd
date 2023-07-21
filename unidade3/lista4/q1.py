#Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada aluno e imprimi-los na ordem inversa.
qtd_alunos = int(input("Digite a quantidade de alunos: "))

alunos = []

for i in range(qtd_alunos):
    nome_aluno = input("Digite o nome do aluno: ")
    alunos.append(nome_aluno)

print("Nomes dos alunos em ordem inversa:")
for aluno in reversed(alunos):
    print(aluno)

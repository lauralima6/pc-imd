#Em uma turma de alunos que conversavam muito, um professor montou a seguinte estratégia. Após os alunos se sentarem, ele mandava os alunos trocarem de lugar. Para ajudar esse processo, crie um programa para ajudar esse professor. O programa deve ler um valor N, que representa a quantidade de alunos. Em seguida, deve ler os nomes de cada aluno. Considere a sequência lida como a ordem das cadeiras dos alunos. O programa deve então imprimir os nomes em uma nova ordem, trocando os alunos sentados em cadeiras de número par (o da primeira cadeira par vai para a última par, o da segunda para a antepenúltima, etc.).
#Se houver uma quantidade ímpar de cadeiras pares (em uma turma de 7 alunos, vão haver 3 cadeiras pares), o aluno da cadeira central não terá seu local trocado.
quantidade_alunos = int(input("Digite a quantidade de alunos: "))

alunos = []

for i in range(quantidade_alunos):
    nome_aluno = input("Digite o nome do aluno: ")
    alunos.append(nome_aluno)

quantidade_cadeiras_pares = quantidade_alunos // 2

for i in range(quantidade_cadeiras_pares):
    if quantidade_alunos % 2 == 0:
        indice_aluno_atual = i * 2
        indice_aluno_troca = quantidade_alunos - 2 - i * 2
    else:
        if i == quantidade_cadeiras_pares - 1:
            break
        indice_aluno_atual = i * 2
        indice_aluno_troca = quantidade_alunos - 3 - i * 2

    alunos[indice_aluno_atual], alunos[indice_aluno_troca] = alunos[indice_aluno_troca], alunos[indice_aluno_atual]

print("Nova ordem dos alunos:")
for aluno in alunos:
    print(aluno)

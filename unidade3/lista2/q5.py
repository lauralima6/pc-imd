#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
nome_atleta = input("Digite o nome do atleta: ")
notas = []

for i in range(7):
    nota = float(input(f"Digite a nota do jurado {i + 1}: "))
    notas.append(nota)
    
notas.sort()

print(f"Resultado final: ")
print(f"Atleta: {nome_atleta}")
print(f"A pior nota é: {notas[0]}")
print(f"A melhor nota é: {notas[6]}")

notas = notas[1:6]

media = sum(notas) / len(notas)

print(f"A média é: {media}")

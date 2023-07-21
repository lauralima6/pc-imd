#Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.
#Formato de entrada
#A primeira entrada é o número de jogadores N (N >= 1). Em seguida, para cada jogador, deve-se se ler uma linha com as seguintes informações: nome do jogador, os valores S, B e A, representam a quantidade de tentativas de saques, bloqueios e ataques; os valores S1, B1 e A1, representando o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.
#Formato de saída
#A saída deve mostrar o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo.
def calcular_percentual(total, sucesso):
    if total == 0:
        return 0
    return (sucesso / total) * 100

n = int(input("Informe a quantidade de jogadores: "))

total_saques = 0
total_saques_sucesso = 0
total_bloqueios = 0
total_bloqueios_sucesso = 0
total_ataques = 0
total_ataques_sucesso = 0

for _ in range(n):
    nome_jogador = input("Nome do jogador:")
    s, b, a, s1, b1, a1 = map(int, input("Digite os dados do jogador").split())

    total_saques += s
    total_saques_sucesso += s1
    total_bloqueios += b
    total_bloqueios_sucesso += b1
    total_ataques += a
    total_ataques_sucesso += a1

percentual_saques = calcular_percentual(total_saques, total_saques_sucesso)
percentual_bloqueios = calcular_percentual(total_bloqueios, total_bloqueios_sucesso)
percentual_ataques = calcular_percentual(total_ataques, total_ataques_sucesso)

print(f"Saques: {percentual_saques:.2f}%")
print(f"Bloqueios: {percentual_bloqueios:.2f}%")
print(f"Ataques: {percentual_ataques:.2f}%")

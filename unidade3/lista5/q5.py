#Muitos algoritmos de I.A. e Aprendizagem de máquina precisam identificar padrões de informação. Um dos mecanismos desses algoritmos, chamados de classificadores, é agrupar dados similares, ou seja "próximos" uns dos outros. Uma informação pode ter várias propriedades (ou características). Por exemplo, uma pessoa pode ser representada pelo seu peso, idade, altura, índice de massa corpórea e assim por diante. Cada propriedade dessa é considerada uma "dimensão" na busca por "similaridade".
#Levando em conta apenas uma dimensão, o primeiro passo da tarefa de encontrar a similaridade (ou proximidade) de dados é encontrar, dentro de uma lista de valores, o par mais próximo um do outro, ou seja aquele cuja diferença é a menor possível. Por exemplo, o par mais próximo na lista [ 4, 9, 1, 7 ] é 9 e 7, que possui diferença de 2. Qualquer outro par de valores da lista terá uma diferença maior que 2.
#Escreva um programa que lê uma um número N seguido por uma lista de N valores e apresenta o par mais próximo. Mesmo que haja mais de um par igualmente próximo, basta apresentar um cuja diferença seja a mínima. No último exemplo de entrada e saída, há dois pares diferentes, mas apenas um é apresentado.
#Divida seu programa em pelo menos duas funções da seguinte forma:
#- Uma função deve ser usada para ler o valor de N e os N números, essa função deve retornar a lista de valores lidos
#- Uma função que recebe a lista de valores e retorna outra lista contendo o par mais próximo
def ler_valores():
    n = int(input("Digite a quantidade de valores: "))
    valores = []
    for _ in range(n):
        valor = float(input("Digite um valor: "))
        valores.append(valor)
    return valores

def encontrar_par_mais_proximo(valores):
    par_mais_proximo = (valores[0], valores[1])
    menor_diferenca = abs(valores[0] - valores[1])
    
    for i in range(len(valores)):
        for j in range(i+1, len(valores)):
            diferenca = abs(valores[i] - valores[j])
            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
                par_mais_proximo = valores[i], valores[j]
    
    return par_mais_proximo

valores = ler_valores()
par_mais_proximo = encontrar_par_mais_proximo(valores)

print("O par mais próximo é:", par_mais_proximo)

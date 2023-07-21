#Para analisar dados coletados (amostras) por estudos científicos, é bastante comum o uso de boxplots, elementos gráficos que exibem os seguintes dados sobre uma amostra:
#- limite superior
#- limite inferior
#- 1º quartil (valor que se encontra na posição 1/4 do conjunto, considerando o conjunto em ordem crescente)
#- 2o quartil/mediana (valor que se encontra na metade do conjunto, considerando o conjunto em ordem crescente)
#- 3º quartil (valor que se encontra na posição 3/4 do conjunto, considerando o conjunto em ordem crescente)
#Nesse contexto, crie um programa que lê um conjunto de N números (N > 2). Para isso, o programa deve primeiro ler o valor de N e depois a lista de N números reais (float). Os dados devem ser informados na ordem crescente, ou seja, do menor valor para o maior, podendo haver elementos repetidos. Em seguida, o programa deve realizar a análise dos dados mostrando as informações presentes em um boxplot (limite inferior, o 1º quartil, a mediana, o 3º quartil e o limite superior), considerando o seguinte:
#Em qualquer iteração do laço de leitura dos N valores, se o valor lido for menor que o anterior, exiba a mensagem:
#"Erro! Conjunto tem de estar em ordem crescente"
#E pare o programa.
import statistics

def calcular_limites(valores):
  limite_inferior = valores[0]
  limite_superior = valores[-2]   
  return limite_inferior, limite_superior
    
def ler_dados_ordenados():
    n = int(input("Digite o valor de N (maior que 2): "))
    dados = []
    anterior = float(input("Digite o primeiro valor: "))
    dados.append(anterior)

    for _ in range(n-1):
        valor = float(input("Digite o próximo valor: "))
        if valor < anterior:
            print("Erro! Conjunto tem de estar em ordem crescente")
            exit()
        dados.append(valor)
        anterior = valor

    return dados
    
def calcular_mediana(valores):
    n = len(valores)
    if n % 2 == 0:
        indice_1 = n // 2 - 1
        indice_2 = n // 2
        mediana = (valores[indice_1] + valores[indice_2]) / 2
    else:
        indice = n // 2
        mediana = valores[indice]
    return mediana

def calcular_quartis(valores):
    n = len(valores)
    quartil_1 = valores[round(n * 1/4)] - 1
    quartil_3 = valores[round(n * 3/4)]
    return quartil_1, quartil_3

def main():
    dados = ler_dados_ordenados()
    limite_inferior, limite_superior = calcular_limites(dados)
    quartil_1, quartil_3 = calcular_quartis(dados)
    mediana = calcular_mediana(dados)

    print("Limite inferior:", limite_inferior)
    print("1º quartil:", quartil_1)
    print("Mediana:", mediana)
    print("3º quartil:", quartil_3)
    print("Limite superior:", limite_superior)

if __name__ == "__main__":
    main()

#Escreva um programa que pede ao usuário um número de dias e converte esse número em semanas e dias. Observe que existem muitos casos específicos a serem tratados, uma vez que faz diferença dizer "dia" ou "dias", bem como "semana" ou "semanas", por exemplo:
#Se o usuário digitar 0, o programa deve exibir: 0 dias equivale à nenhum dia.
#Se o usuário digitar 7, o programa deve exibir: 7 dias equivalem à 1 semana!
#Se o usuário digitar 8, o programa deve exibir: 8 dias equivalem à 1 semana e 1 dia!
#Se o usuário digitar 30, o programa deve exibir: 30 dias equivalem à 4 semanas e 2 dias!
def converter_dias_semanas(dias):
    semanas = dias // 7
    dias_restantes = dias % 7

    if semanas == 1:
        semanas_str = "semana"
    else:
        semanas_str = "semanas"

    if dias_restantes == 1:
        dias_str = "dia"
    else:
        dias_str = "dias"

    return f"{semanas} {semanas_str} e {dias_restantes} {dias_str}."

numero_dias = int(input("Digite o número de dias: "))
resultado = converter_dias_semanas(numero_dias)
print(resultado)

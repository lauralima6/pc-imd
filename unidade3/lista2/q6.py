#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
#resultado da operação solicitada.
def calcular_operacao(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Erro: Operação inválida!"

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    resultado = calcular_operacao(num1, num2, operacao)
    print("Resultado:", resultado)

main()


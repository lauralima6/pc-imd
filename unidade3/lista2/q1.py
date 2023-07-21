#Escreva um programa que lê do usuário 3 números e imprime quem é o maior, quem é o menor e quem é o do 'meio'. Veja que existem diferentes casos a considerar: (1) três números iguais, (2) três números diferentes, (3) dois números iguais. Para cada um dos casos seu programa deve imprimir a saída de acordo com os exemplos que seguem:
def encontra_maior_menor_meio(num1, num2, num3):
    if num1 == num2 == num3:
      
        print("Os três números são iguais.")
        print(f"Maior: {num1}")
        print(f"Menor: {num1}")
        print("Não há número do 'meio'.")

    elif num1 != num2 and num1 != num3 and num2 != num3:
        
        maior = max(num1, num2, num3)
        menor = min(num1, num2, num3)
        meio = num1 + num2 + num3 - maior - menor

        print("Os três números são diferentes.")
        print(f"Maior: {maior}")
        print(f"Menor: {menor}")
        print(f"Número do meio: {meio}")

    else:
      
        if num1 == num2:
            maior = max(num1, num3)
            menor = min(num1, num3)
            meio = num1
        elif num1 == num3:
            maior = max(num1, num2)
            menor = min(num1, num2)
            meio = num1
        else:  
            maior = max(num1, num2)
            menor = min(num1, num2)
            meio = num2

        print("Dois números são iguais.")
        print(f"Maior: {maior}")
        print(f"Menor: {menor}")
        print(f"Não há elementos no meio")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

encontra_maior_menor_meio(num1, num2, num3)

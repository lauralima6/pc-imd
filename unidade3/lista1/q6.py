#Faça um programa que transforme uma temperatura fornecida em Celsius para a correspondente em Fahrenheit.
#A formula de conversão de Celsius para Fahrenheit é a seguinte: C=(5/9)*(F– 32).
temp = float(input('Forneça a temperatura em Celsius: '))
conversaoF = (temp * 1.8) + 32
print('A conversão de {}°C para Fahrenheit é: {}°F'.format(temp, conversaoF))
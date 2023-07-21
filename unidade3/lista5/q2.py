#O engenheiro de Software pediu para organizarmos o código usando funções simples, mas sem usar variáveis globais. Assim o código deve ter as seguintes funções:
def exibeOpcoes():
    print('Qual operação você deseja realizar?')
    print('1 - SAQUE')
    print('2 - DEPÓSITO')
    print('3 - SALDO')
    print('4 - SAIR')
    opcao = int(input('Escolha: '))
    return opcao

def processaOpcoes(opcao, saldo):
    if opcao == 1:
        saldo = saque(saldo)
    elif opcao == 2:
        saldo = deposito(saldo)
    elif opcao == 3:
        exibeSaldo(saldo)
    elif opcao == 4:
        print('Obrigado por usar os serviços do Caixa Eletrônico')
        exit()
    else:
        print('Opção inválida, tente novamente!')
    return saldo

def exibeSaldo(saldo):
    print('O seu saldo atual é de:', saldo)

def saque(saldo):
    valor_sacado = float(input('Qual valor você deseja sacar? '))
    if valor_sacado <= saldo:
        saldo -= valor_sacado
        print('Saque autorizado. Agora o seu saldo atual é de:', saldo)
    else:
        print('Saldo insuficiente.')
    return saldo

def deposito(saldo):
    valor_deposito = float(input('Qual o valor que você quer depositar? '))
    if valor_deposito > 0:
        saldo += valor_deposito
        print('O seu saldo agora é de:', saldo)
    else:
        print('Valor inválido')
    return saldo

def principal():
    saldo = 1000
    while True:
        opcao = exibeOpcoes()
        saldo = processaOpcoes(opcao, saldo)

principal()

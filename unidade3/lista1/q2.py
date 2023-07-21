#Monte uma tabela-verdade com os valores de A AND B e A OR B por meio de um programa. Para isso, seu programa deve receber o valor booleano para as variáveis A e B e então imprimir na tela os valores respectivos para cada operação (AND e OR), como no exemplo.
def boolean_to_int(value):
    if value == False:
        return 0
    elif value == True:
        return 1
    else:
        raise ValueError("Valores diferentes de True (1) e False (0) não são permitidos.")

def int_to_boolean(value):
    if value == 0:
        return False
    elif value == 1:
        return True
    else:
        raise ValueError("Valores diferentes de 0 e 1 não são permitidos.")

def print_table(a, b):
    print("Tabela-Verdade:")
    print(f"A = {int_to_boolean(a)}, B = {int_to_boolean(b)}")
    print("A AND B:", int_to_boolean(a and b))
    print("A OR B:", int_to_boolean(a or b))

try:
    A = boolean_to_int(bool(int(input("Digite o valor de A (0 para False, 1 para True): "))))
    B = boolean_to_int(bool(int(input("Digite o valor de B (0 para False, 1 para True): "))))

    print_table(A, B)

except ValueError as e:
    print("Erro:", e)

    
    
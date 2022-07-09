"""Calculadora Infix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py mul 10 5
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""

___version___ = "0.1.0"

import sys
import os
from datetime import datetime


while True:
    arguments = sys.argv[1:]

    # Validação
    if not arguments:
        op = input('Operação: ')
        n1 = input('n1: ')
        n2 = input('n2: ')

        arguments = [op,n1, n2]

    elif len(arguments) != 3:
        print('Quantidade de args inválido')
        sys.exit(1)

    operation, *numeros = arguments

    op_list = ['sum', 'sub', 'mul', 'div']

    if (operation not in op_list):
        print(f'Operação inválida, informe um dos itens a seguir {op_list}')
        sys.exit(1)

    validate_nums = []
    for num in numeros:
        if not num.replace('.', '').isdigit(): #replace para que não saia do programa caso seja digitado um valor float
            print(f'Número inválido {num}')
            sys.exit(1)
        if "." in num:
            num = float(num)    
        else:
            num = int(num)
        validate_nums.append(num)

    num1, num2 = validate_nums

    if(operation == 'sum'):
        result = num1 + num2
    elif(operation == 'sub'):
        result = num1 - num2
    elif(operation == 'mul'):
        result = num1 * num2
    else: 
        result = num1 / num2

    print(f"O resultado é {result}")

    path = os.curdir #diretório atual
    filepath = os.path.join(path, "infixcalc.log")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = os.getenv('USERNAME', 'anonymous')

    try:
        with open(filepath, 'a') as file_calc:
            file_calc.write(f"{timestamp} - {user} - {operation}, {num1}, {num2} = {result}\n")
    except PermissionError as e:
        print(str(e))
        sys.exit(1)
        
    cont = input("Deseja efetuar outra operação? [N/y]").strip().lower()
    if cont != 'y':
        break
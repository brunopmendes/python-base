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
"""

___version___ = "0.1.0"

import sys

arguments = sys.argv[1:]

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

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

if(operation == 'sum'):
    print(sum)
elif(operation == 'sub'):
    print(sub)
elif(operation == 'mul'):
    print(mul)
else:
    print(div)
"""Calculadora infix.
Funcionamento:
[operacao] [n1] [n2]
Operacoes:
sum -> +
sub -> -
mul -> *
div -> /
Uso:
$ infixcalc.py sum 5 2
7
$ infixcalc.py mul 10 5
50
$ infixcalc.py 
operacao: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("operacao:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Numero de argumentos invalidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operacao invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repeticao while + exceptions
    if not num.isdigit():
        print(f"Numero invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)

# TODO: Usar dict de funcoes
if operation == "sum":
    print(n1 + n2)
elif operation == "sub":
    print(n1 - n2)
elif operation == "mul":
    print(n1 * n2)
elif operation == "div":
    print(n1 / n2)
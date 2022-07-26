def outra_funcao(a, b, c):
    """Explica o que função faz"""
    # tupla como valor de retorno
    return a * 2, b * 2, c * 2

valor1, *resto = outra_funcao(1, 2, 3)
print(valor1)
print(resto)

##########################

def soma(n1, n2):
    """Faz a soma de dois números"""
    return n1 + n2

# normal
print(soma(10, 20)) 

# argumentos em sequência
args = (20, 30) #tuple
print(soma(*args)) 

# argumentos dicionario / nomeados
args_dict = {"n1": 90, "n2": 100}
print(soma(**args_dict))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
    (5, 10),
    [8, 13],
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))
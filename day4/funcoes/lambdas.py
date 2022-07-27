from unicodedata import name


names = ["Bruno", "Carlos", "Danilo", "Antonio", "Joubert"]

# print(sorted(names)) #ordem alfabetica

# print(sorted(names, key=len)) #ordem por tamanho

# print(sorted(names, key=lambda name: name.count("i"))) #ordem por nomes que possuem letra i

# print(list(map(lambda name: "Hello, " + name, names)))


# Calculadora
operacao = input("operacao (sum, mul, div sub)").strip()
n1 = input("n1: ").strip()
n2 = input("n2: ").strip()

operacoes = {
    "sum": lambda a, b: a + b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
    "sub": lambda a, b: a - b,
}

resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é: {resultado}")
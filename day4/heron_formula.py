import math

def heron_formula(a, b, c):
    # Cálcula a área de um triângulo
    perimeter = a + b + c
    s = perimeter/2

    area = s * (s - a) * (s - b) * (s - c)
    return math.sqrt(area)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
]

for idx, t in enumerate(triangulos):
    print(f"A área do triângulo {idx + 1} é {heron_formula(*t)}")
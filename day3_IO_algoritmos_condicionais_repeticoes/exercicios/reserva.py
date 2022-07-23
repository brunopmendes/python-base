"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos disponíveis
para alugar e o preço de cada quarto, esta informação está disponível em um aquivo de texto
separado por vírgulas.

`quartos.txt`

codigo, nome, preco
1, Suite Master, 500
2, Quarto Familia, 200
3, Quarto Single, 100
4, Quarto Simples, 50


O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final eibe o vxalor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`

cliente, quarto, dias
Bruno, 3, 12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""

import logging
import sys


ocupados = {}
try:
    for line in open('reservas.txt'):
        nome, num_quarto, dias = line.strip().split(',')
        ocupados[int(num_quarto)] = {
            'nome': nome,
            'dias': dias
        }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe")
    sys.exit(1)


quartos = {}
try:
    for line in open('quartos.txt'):
        codigo, nome, preco = line.split(',')
        quartos[int(codigo)] = {
            'nome': nome,
            'preco': float(preco), # TODO: Decimal
            'disponivel': False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)

print("Reserva Hotel Mendes")
print("-" * 50)

if len(ocupados) == len(quartos):
    print("Hotel sem quartos disponíveis")
    sys.exit(1)

cliente_name = input("Informe seu nome: ").strip()

print("Lista de quartos:")
for codigo, dados in quartos.items():
    nome_quarto = dados['nome']
    preco = dados['preco']
    disponivel = "⛔" if not dados['disponivel'] else "👍"
    # TODO: Substituir casa decimal por vírgula
    print(f"{codigo} - {nome_quarto} - {preco:.2f} - {disponivel}")


print("-" * 50)
try:
    num_quarto = int(input("Informe o número do quarto a ser reservado: ").strip())

    if not quartos[num_quarto]['disponivel']:
        print(f'O quarto {num_quarto} está ocupado.')
        sys.exit(1)

except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)
except KeyError:
    logging.error(f"Quarto {num_quarto} não existe")
    sys.exit(1)

try:
    qtd_dias = int(input("Informe a quantidade de dias de estadia: ").strip())
except ValueError:
    logging.error("Número inválido, digite apenas digitos.")
    sys.exit(1)

nome_quarto = quartos[num_quarto]['nome']
preco_quarto = quartos[num_quarto]['preco']
disponivel = quartos[num_quarto]['disponivel']

with open('reservas.txt', 'a') as file_:
    file_.write(f"{cliente_name},{num_quarto},{qtd_dias}\n")

print(f"{cliente_name} você escolheu o quarto {nome_quarto} e vai custar R$ {(preco_quarto * qtd_dias):.2f}")
"""Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e
o índice de umidade do ar sendo quw, será exibida uma mensagem de alerta
dependendo das condições:

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA: Frio extremo
"""

import sys
import logging
log = logging.Logger("alerta")

# try:
#     temp_atual = float(input("Informe a temperatura atual: ").strip())
# except ValueError as e:
#     log.error("Temperatura inválida")
#     sys.exit(1)

# try:
#     umidade_atual = float(input("Informe a umidade do ar: ").strip())
# except ValueError as e:
#     log.error("Umidade inválida")
#     sys.exit(1)

info = {
    "temperatura": None,
    "umidade": None
}

while True:
    # condicao de parada
    # o dicionário está completamente preenchido
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])

    if info_size == filled_size:
        break

    keys = info.keys()
    for key in keys:

        if info[key] is not None:
            continue
        try:
            info[key] = float(input(f"Informe a {key}: ").strip())
        except ValueError:
            log.error(f"{key.capitalize()} inválida")
            sys.exit(1)

temp = info['temperatura']
umi = info['umidade']

if temp > 45:
    print("ALERTA!!! Perigo calor extremo")
elif (temp * 3) >= umi:
    print("ALERTA!!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp <= 9:
    print("Frio")
else:
    print("Frio extremo")
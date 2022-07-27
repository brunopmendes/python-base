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

# TODO: Mover para módulo de utilidades

def is_completely_filled(dict_of_inputs):
    """Returns a boolean telling if a dict is completely filled"""
    info_size = len(dict_of_inputs)
    filled_size = len(
        [value for value in dict_of_inputs.values() if value is not None]
    )
    dict_full = info_size == filled_size
    return dict_full

def read_inputs_for_dict(dict_of_info):
    """reads information for a dict from user inputs"""
    for key in dict_of_info.keys(): #["temperatura", "umidade"]

        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = float(input(f"Informe a {key}: ").strip())
        except ValueError:
            log.error(f"{key.capitalize()} inválida")
            sys.exit(1)

# PROGRAMA PRINCIPAL
info = {"temperatura": None, "umidade": None}

while not is_completely_filled(info):
    read_inputs_for_dict(info)

temp, umi = info.values()

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
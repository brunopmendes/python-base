""" Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
    python hello.py
"""

#Metadados default
__version__ = "0.1.0"
__author__ = "Bruno Mendes"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5] #caso a variável não existe, por defaul terá en_US

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bounjour Monde"

print(msg)
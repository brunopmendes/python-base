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

current_language = os.getenv("LANG", "en_US")[:5] #caso a variável não existe, por default será en_US

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

print(msg[current_language])
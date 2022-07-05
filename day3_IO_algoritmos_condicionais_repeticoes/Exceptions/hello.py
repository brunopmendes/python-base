"""
Hello World Multi Linguas.
Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.
Como usar:
Tenha a variavel LANG devidamente configurada:
    export LANG=pt_BR
Ou informe atraves do CLI argument `--lang`
Ou o usuario tera que digitar.
Execucao:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Bruno Mendes"
__license__ = "Unlicense"

from email import message
import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed  {arg}")
        print("Try with --key=value")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repeticao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Ola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde",
}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
"""Imprime a mensagem de um e-mail
"""

___version___ = "0.1.1"

import os
import sys
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]

if not arguments:
    print("Informe o nome do arquivo de emails e nome do template")
    sys.exit(1)
if len(arguments) != 2:
    print("Quantidade de argumentos inválida. \nInforme o nome do arquivo de email e nome do template")
    sys.exit(1)

filename = arguments[0]
template_name = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
template_path = os.path.join(path, template_name) #email_template.txt

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath):  #c/ open o for itera linha por linha do arquivo txt
        name, email = line.split(",")

        text = (
            open(template_path).read()
            % {
                "nome": name,
                "produto": "caneta",
                "texto": "sua ausencia de caneta.",
                "link": "https://caneta.com.br",
                "quantidade": 1,
                "preco": 50,
            }
        )


        FROM = "brupmendes@gmail.com"
        TO = ", ".join([email])
        SUBJECT = "Compre +"
        message = MIMEText(text)
        
        message["Subject"] = f"{SUBJECT}"
        message["From"] = f"{FROM}"
        message["To"] = f"{TO}"

        server.sendmail(FROM, TO, message.as_string())

    
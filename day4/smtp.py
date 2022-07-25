"""Exemplos de envio de e-mail"""

# comando p/ configurar o servidor para envio local
# python -m smtpd -c DebuggingServer -n localhost:8025

import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "brupmendes@gmail.com"
TO = ["brupmendes@icloud.com", "bruninho9802008@hotmail.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Hello World!</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message)
#!usr/bin/env python 3

import os
import logging
from logging import handlers

# BOILERPLATE - Códigos repetitivos
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(__name__, log_level)
# ch = logging.StreamHandler() #Console/terminal
# ch.setLevel(log_level) #seta level do handler

file_handler = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=100, # 10**6 -> 1GB
    backupCount=10
)
file_handler.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt) #formatacao handler
file_handler.setFormatter(fmt) #formatacao handler
# log.addHandler(ch)
log.addHandler(file_handler)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

print("-" * 20)

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))

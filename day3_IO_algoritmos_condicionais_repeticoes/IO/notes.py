"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: 
Anotacao geral sobre carreira de tecnologia

$ notes.py read --tag==tech
"""

___version___ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

commands = ("read", "new")
if len(arguments) != 2:
    print("Invalid argument numbers")
    sys,exit(1)
elif arguments[0] not in commands:
    print(f"Invalid argument {arguments[0]}")
    sys,exit(1)

if arguments[0] == "read":

    tag_arg = arguments[1]
    # leitura das notas
    for line in open(filepath):  #c/ open o for itera linha por linha do arquivo txt
        title, tag, text = line.split(",")

        if(tag_arg == tag):
            print(f"{title} \n{tag} \n{text}")
            print("-" * 50)

if arguments[0] == "new":
    # criação da nota
    title = arguments[1] #TODO: Tratar exception
    tag = input("tag: ").strip()
    text = input("text:").strip()

    with open(filepath, "a") as file_notes:
        file_notes.write(f"{title},{tag},{text}\n")
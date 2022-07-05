___version___ = "0.1.1"

import os
import sys

commands = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {commands}")
    sys.exit(1)

if arguments[0] not in commands:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if(tag.lower() == arguments[1].lower()):
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 50)


if arguments[0] == "new":
    title = arguments[1] #TODO: Tratar exception
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
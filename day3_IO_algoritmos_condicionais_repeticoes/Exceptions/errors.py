#!/usr/bin/env python3

import os
import sys
import logging
import time

log = logging.Logger("errors")

# EAFP - Easy to Ask Forgiveness than permission

def try_to_open_file(file_path, retry=1):
    """Tries to open a file, if error, retries n times"""
    for attempt in range(1, retry + 1):
        try:
            return open(file_path).readlines() # FileNotFoundError
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
            time.sleep(1)
        else:
            print("Sucesso!")
        finally:
            print("Execute isso sempre!")
    return []

for line in try_to_open_file("names.txt", 5):
    print(line)
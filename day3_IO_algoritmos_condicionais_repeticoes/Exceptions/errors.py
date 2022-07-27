#!/usr/bin/env python3

from argparse import ArgumentError
import os
import re
import sys
import logging
import time

log = logging.Logger("errors")

# EAFP - Easy to Ask Forgiveness than permission

def try_to_open_file(file_path, retry=1):
    """Tries to open a file, if error, retries n times"""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")

    try:
        return open(file_path).readlines() # FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            # recursao
            try_to_open_file(file_path, retry=retry-1)
    else:
        print("Sucesso!")
    finally:
        print("Execute isso sempre!")
    return []

for line in try_to_open_file("names.txt", 5):
    print(line)
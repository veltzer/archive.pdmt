"""
Helper to print messages on the command line
"""

import sys


def print_msg(msg):
    print(f'pdmt: {msg}')


def print_msg_noeol_flush(msg):
    print(f'pdmt: {msg}', end='')
    sys.stdout.flush()


def print_raw(msg):
    print(msg)

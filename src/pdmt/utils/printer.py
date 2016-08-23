'''
Helper to print messages on the command line
'''

import sys # for stdout

def print_msg(msg):
    print('pdmt: {msg}'.format(msg=msg))
def print_msg_noeol_flush(msg):
    print('pdmt: {msg}'.format(msg=msg), end='')
    sys.stdout.flush()
def print_raw(msg):
    print(msg)

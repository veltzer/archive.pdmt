'''
Helper to print messages on the command line
'''

def print_msg(msg):
	print('pdmt: {msg}'.format(msg=msg))
def print_msg_noeol(msg):
	print('pdmt: {msg}'.format(msg=msg), end='')
def print_raw(msg):
	print(msg)

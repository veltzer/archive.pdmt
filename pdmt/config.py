import imp
import os

imp.load_source('pdmt.config','pdmt/cfg.py')
overridefiles=os.path.expanduser('~/.cfg.py')
if os.path.isfile(overridefiles):
	imp.load_source('pdmt.config',overridefiles)

def show():
	for ns_name in pdmt.config.__dict__:
		#if not ns_name.startswith('__'):
		if ns_name.startswith('ns_'):
			print(ns_name)
			ns=pdmt.config.__dict__[ns_name]
			for p in ns.__dict__:
				#if not p.startswith('__'):
				if p.startswith('p_'):
					print('\t',p,ns.__dict__[p])

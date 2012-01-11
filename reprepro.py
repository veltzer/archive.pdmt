#!/usr/bin/python

import subprocess
import argparse
import sys # for argv

parser=argparse.ArgumentParser(description='manage debian archive')
parser.add_argument(
		'--install',
		help='install package',
		action='store_true',
		default=False,
)
parser.add_argument(
		'--remove',
		help='remove package',
		action='store_true',
		default=False,
)
parser.add_argument(
		'--dumpunreferenced',
		help='dump unreferenced',
		action='store_true',
		default=False,
)
parser.add_argument(
		'--deleteunreferenced',
		help='delete unreferenced',
		action='store_true',
		default=False,
)
parser.add_argument(
		'--deb',
		help='debian file to install',
		default=None,
)
parser.add_argument(
		'--name',
		help='cannonical name of debian package to remove',
		default=None,
)
parser.add_argument(
		'--redirect',
		help='redirect stdout and stderr',
		action='store_true',
		default=True,
)
parser.add_argument(
		'--component',
		help='what apt component to work on',
		default='main',
)
parser.add_argument(
		'--codename',
		help='what apt component to work on',
		# TODO - get it from the OS
		default='oneiric',
)
parser.add_argument(
		'--servicedir',
		help='what directory to work on',
		default='/var/www/apt',
)
options=parser.parse_args()
if sum([options.install,options.remove,options.dumpunreferenced,options.deleteunreferenced])!=1:
	parser.error('must specify')
if options.install:
	if options.deb==None:
		parser.error('must specify --deb')
if options.remove:
	if options.deb==None:
		parser.error('must specify --deb')

args=[]
args.append('sudo');
args.append('reprepro');
args.extend(['--basedir',options.servicedir])
if options.install:
	args.extend(['--component',options.component])
	args.extend(['includedeb',options.codename,options.deb])
if options.remove:
	args.extend(['--component',options.component])
	args.extend(['remove',options.codename,options.name]);
if options.dumpunreferenced:
	args.append('dumpunreferenced');
if options.deleteunreferenced:
	args.append('deleteunreferenced');
kw={}
if options.redirect:
	kw['stderr']=open('/dev/null')
	kw['stdout']=open('/dev/null')
subprocess.check_call(args,**kw)

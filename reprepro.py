#!/usr/bin/python

import subprocess
import optparse

parser=optparse.OptionParser()
parser.add_option(
		"-i","--install",
		help="install package",
		action="store_true",
		default=False,
)
parser.add_option(
		"-r","--remove",
		help="remove package",
		action="store_true",
		default=False,
)
parser.add_option(
		"-u","--dumpunreferenced",
		help="dump unreferenced",
		action="store_true",
		default=False,
)
parser.add_option(
		"-d","--deleteunreferenced",
		help="delete unreferenced",
		action="store_true",
		default=False,
)
parser.add_option(
		"-y","--redirect",
		help="redirect stdout and stderr",
		action="store_true",
		default=False,
)
(options,args)=parser.parse_args()
if sum([options.install,options.remove,options.dumpunreferenced,options.deleteunreferenced])!=1:
	parser.error("must specify")

# params
p_debfile='deb_dist/python-pdmt_1-1_all.deb'
p_debname='python-pdmt'
p_component='main'
p_servicedir='/var/www/apt'
p_codename='oneiric'

args=[]
args.append('sudo');
args.append('reprepro');
args.extend(['--basedir',p_servicedir])
if options.install:
	args.extend(['--component',p_component])
	args.extend(['includedeb',p_codename,p_debfile])
if options.remove:
	args.extend(['--component',p_component])
	args.extend(['remove',p_codename,p_debname]);
if options.dumpunreferenced:
	args.append('dumpunreferenced');
if options.deleteunreferenced:
	args.append('deleteunreferenced');
kw={}
if options.redirect:
	kw['stderr']=open('/dev/null')
	kw['stdout']=open('/dev/null')
subprocess.check_call(args,**kw)

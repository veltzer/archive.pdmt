#!/usr/bin/python3

# this script will install all the required packages that you need on
# ubuntu to compile and work with this package.

import subprocess # for check_call

packs=[
	# packages needed to build .debs from python code
	'devscripts',
	'python-pydot', # for dot graph generation
	'python-all-dev',
	'python-stdeb',
	'build-essential',
	'dpkg-dev',
	'debhelper',
	'fakeroot',
	'cdbs',
	'git-buildpackage',
]

args=['sudo','apt-get','install']
args.extend(packs)
subprocess.check_call(args)

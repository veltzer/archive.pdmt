#!/usr/bin/python3

# this script will install all the required packages that you need on
# ubuntu to compile and work with this package.

import subprocess # for check_call

packs=[
	# curses and text gui
	'python3-progressbar',
	'python-progressbar',

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

	# docbook stuff
	'docbook5-xml',
	'docbook-xsl-ns',
	'docbook-defguide',
	'xsltproc',
	'fop',
	'xmlto',
	'libxml2-utils',
	'xmlstarlet',
	'pandoc',

	# cmd2 stuff
	'python3-cmd2',
	'python-cmd2',

	# inotify
	'python-pyinotify',
	'python3-pyinotify',
	'python-pyinotify-doc',

	# graph
	'python3-pygraph',
	'python-pygraph',
	'python-igraph',

	# profiling
	'python3-objgraph',
	'python-objgraph',
	'python-objgraph-doc',
	'python3-memprof',
	'python-memprof',
	'python3-psutil',
	'python-psutil',

	# other tools
	'scons',
	'gradle',
	'maven',
]

args=['sudo','apt-get','install']
args.extend(packs)
subprocess.check_call(args)

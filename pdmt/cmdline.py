import argparse
import utils.installer
import utils.debmaker
import sys

# see documentation in http://docs.python.org/library/argparse.html

def parse(mgr):
	parser=argparse.ArgumentParser(description='Project Dependency Management Tool')
	parser.add_argument(
			'--clean',
			help='clean project',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--build',
			help='build project',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--dumpgraph',
			help='dump graph',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--dumpoperations',
			help='dump operations',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--install',
			help='install',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--interactive',
			help='start interactive mode',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--deb',
			help='build debian package',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--installdeb',
			help='install the deb package into a repository',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--runop',
			metavar='operation',
			help='run an operation',
			action='store',
			default=None,
	)
	options=parser.parse_args()
	#print options
	#sys.exit(1)
	runop_int=0
	if options.runop is not None:
		runop_int=1
	if sum([
		options.clean,
		options.build,
		options.dumpgraph,
		options.dumpoperations,
		options.install,
		options.deb,
		options.installdeb,
		runop_int,
	])!=1:
		parser.error('must specify one of clean,build,dumpgraph,dumpoperations,install,deb,runop')
	if options.clean:
		mgr.clean()
	if options.build:
		mgr.build()
	if options.dumpgraph:
		mgr.dumpgraph()
	if options.dumpoperations:
		mgr.dumpoperations()
	if options.install:
		utils.installer.doit()
	if options.deb:
		utils.debmaker.doit()
	if options.installdeb:
		utils.reprepro.doit()
	if options.runop:
		mgr.runOperation(options.runop)

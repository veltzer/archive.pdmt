import argparse
import sys

# see documentation in http://docs.python.org/library/argparse.html

def parse(mgr):
	debug=False
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
			'--printgraph',
			help='print the graph (may be long)',
			action='store_true',
			default=False,
	)
	parser.add_argument(
			'--dotgraph',
			help='write the graph to a .dot file',
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
			'--runop',
			metavar='operation',
			help='run an operation',
			action='store',
			default=None,
	)
	options=parser.parse_args()
	if debug:
		print options
		sys.exit(1)
	runop_int=0
	if options.runop is not None:
		runop_int=1
	if sum([
		options.clean,
		options.build,
		options.printgraph,
		options.dotgraph,
		options.dumpoperations,
		runop_int,
	])!=1:
		parser.error('must specify one of clean,build,printgraph,dotgraph,dumpoperations,runop')
	if options.clean:
		mgr.clean()
	if options.build:
		mgr.build()
	if options.printgraph:
		mgr.printgraph()
	if options.dotgraph:
		mgr.dotgraph()
	if options.dumpoperations:
		mgr.dumpoperations()
	if options.runop:
		mgr.runOperation(options.runop)

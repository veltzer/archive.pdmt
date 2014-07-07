import argparse # for ArgumentParser
import sys # for exit

# see documentation in http://docs.python.org/library/argparse.html

##############
# parameters #
##############
debug=False

def parse(mgr):
	parser=argparse.ArgumentParser(description='Project Dependency Management Tool')
	parser.add_argument(
			'--build',
			help='build project',
			action='store_true',
			default=True,
	)
	options=parser.parse_args()
	if debug:
		print(options)
	if sum([
		options.build,
	])!=1:
		parser.error('must specify one of build,showconfig')
	if options.build:
		mgr.build()

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
			'--printnodes',
			help='print all the node names',
			action='store_true',
			default=False,
	)
	options=parser.parse_args()
	if debug:
		print('options are',options)
	mysum=sum([
                options.printnodes,
        ])
	if mysum>1:
		parser.error('only one option at a time')
	if mysum==0:
		mgr.build()
	else:
		if options.printnodes:
			mgr.graph.printnodes()

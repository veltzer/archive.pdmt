import argparse # for ArgumentParser
import sys # for exit, argv

"""
argparse seems to be the right argument parser for python
see documentation in http://docs.python.org/library/argparse.html
"""

##############
# parameters #
##############
def parse(mgr):
	parser=argparse.ArgumentParser(description='Project Dependency Management Tool')
	parser.add_argument(
			'--printnodes',
			help='print all the node names',
			action='store_true',
			default=False,
	)
	# all other arguments are gathered into options.args
	parser.add_argument('args', nargs=argparse.REMAINDER)
	options=parser.parse_args()
	mysum=sum([
                options.printnodes,
        ])
	if mysum>1:
		parser.error('only one option at a time')
	if mysum==0:
		mgr.build()
	else:
		if options.printnodes:
			if options.args:
				parser.error('no free args with --printnodes {0}'.format(str(options.args)))
			else:
				mgr.graph.printnodes()

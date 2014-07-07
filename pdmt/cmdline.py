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
			'--bashcomplete',
			nargs=1,
			help='print all the node names',
	)
	# all other arguments are gathered into options.args
	parser.add_argument('args', nargs=argparse.REMAINDER)
	options=parser.parse_args()
	mysum=sum([
                options.bashcomplete is not None,
        ])
	if mysum>1:
		parser.error('only one option at a time')
	if mysum==0:
		if options.args:
			mgr.build_node_names(options.args)
		else:
			mgr.build()
	else:
		if options.bashcomplete is not None:
			if options.args:
				parser.error('no free args with --bashcomplete {0}'.format(str(options.args)))
			else:
				mgr.graph.bashcomplete(options.bashcomplete[0])

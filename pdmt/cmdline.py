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
		help='help to do bash completions',
	)
	parser.add_argument(
		'--listnodes',
		action='store_true',
		default=False,
		help='help to do bash completions',
	)
	# all other arguments are gathered into options.nodes
	parser.add_argument('nodes', nargs=argparse.REMAINDER)
	options=parser.parse_args()
	mysum=sum([
                options.bashcomplete is not None,
		options.listnodes,
        ])
	if mysum>1:
		parser.error('only one option at a time')
	if mysum==0:
		if options.nodes:
			mgr.build_node_names(options.nodes)
		else:
			mgr.build()
	else:
		if options.bashcomplete is not None:
			if options.nodes:
				parser.error('no node names with --bashcomplete {0}'.format(str(options.nodes)))
			else:
				mgr.graph.bashcomplete(options.bashcomplete[0])
		if options.listnodes:
			mgr.graph.listnodes()

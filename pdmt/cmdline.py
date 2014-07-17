import argparse # for ArgumentParser
import pdmt.exceptions # for CommandLineInputException
import pdmt.tui # for go

'''
argparse seems to be the right argument parser for python
see documentation in http://docs.python.org/library/argparse.html
'''

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
		help='list all nodes in the graph',
	)
	parser.add_argument(
		'--build',
		action='store_true',
		default=False,
		help='build stuff',
	)
	parser.add_argument(
		'--tui',
		action='store_true',
		default=False,
		help='run a command line text user interface',
	)
	# all other arguments are gathered into options.nodes
	parser.add_argument('nodes', nargs=argparse.REMAINDER)
	options=parser.parse_args()
	mysum=sum([
                options.bashcomplete is not None,
		options.listnodes,
		options.build,
		options.tui,
        ])
	if mysum>1:
		parser.error('not more than one option at a time')
	# tui is the default option
	if mysum==0:
		options.tui=True

	if options.bashcomplete is not None:
		if options.nodes:
			parser.error('no node names with --bashcomplete {0}'.format(str(options.nodes)))
		else:
			mgr.bashcomplete(options.bashcomplete[0])

	if options.listnodes:
		mgr.listnodes()

	if options.build:
		if options.nodes:
			try:
				mgr.build_node_names(options.nodes)
			except pdmt.exceptions.CommandLineInputException as e:
				e.print_and_exit()
		else:
			mgr.build()

	if options.tui:
		if options.nodes:
			parser.error('no command line args with tui')
		pdmt.tui.go(mgr)

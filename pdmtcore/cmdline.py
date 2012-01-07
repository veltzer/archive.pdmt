import optparse
def parse(mgr):
	parser=optparse.OptionParser()
	parser.add_option(
			"-c","--clean",
			help="clean project",
			action="store_true",
			default=False,
	)
	parser.add_option(
			"-b","--build",
			help="build project",
			action="store_true",
			default=False,
	)
	parser.add_option(
			"-p","--prnt",
			help="print graph",
			action="store_true",
			default=False,
	)
	parser.add_option(
			"-i","--interactive",
			help="start interactive mode",
			action="store_true",
			default=False,
	)
	(options, args) = parser.parse_args()
	if sum([options.clean,options.build,options.prnt])>1:
		    parser.error("clean build and prnt are mutually exclusive")
	#print options, args
	if options.clean:
		mgr.clean()
	if options.build:
		mgr.build()
	if options.prnt:
		mgr.prnt()

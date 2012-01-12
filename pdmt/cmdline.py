import argparse
import utils.installer
import utils.debmaker

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
			'--dump',
			help='dump graph',
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
	options=parser.parse_args()
	if sum([
		options.clean,
		options.build,
		options.dump,
		options.install,
		options.deb,
	])!=1:
		parser.error('must specify one of clean,build,dump,install,deb')
	if options.clean:
		mgr.clean()
	if options.build:
		mgr.build()
	if options.dump:
		mgr.dump()
	if options.install:
		utils.installer.doit()
	if options.deb:
		utils.debmaker.doit()

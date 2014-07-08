import pdmt.api
import pdmt.utils.subproc
import pdmt.config

"""
This module handles publishing and unpublishing a deb package from an apt repository

	Mark Veltzer <mark@veltzer.net>
"""
class Operation(object):
	def __init__(self):
		super().__init__(
			'debinstaller',
			'install the package into the repository',
		)
	def run(self):
		args=[]
		if pdmt.config.ns_apt.p_sudo:
			args.append('sudo')
		args.append('reprepro')
		args.extend(['--basedir',pdmt.config.ns_apt.p_abs_dir])
		args.extend(['--component',pdmt.config.ns_apt.p_component])
		args.extend(['includedeb',pdmt.config.ns_apt.p_codename,pdmt.config.ns_apt.p_deb_file])
		pdmt.utils.subproc.check_call(args)
	def remove():
		args=[]
		if pdmt.config.ns_apt.p_sudo:
			args.append('sudo')
		args.append('reprepro')
		args.extend(['--basedir',pdmt.config.ns_apt.p_abs_dir])
		args.extend(['--component',pdmt.config.ns_apt.p_component])
		args.extend(['remove',pdmt.config.ns_apt.p_codename,NAME])
		pdmt.utils.subproc.check_call(args)
	def command(name):
		args=[]
		if pdmt.config.ns_apt.p_sudo:
			args.append('sudo')
		args.append('reprepro')
		args.append(name)
		pdmt.utils.subproc.check_call(args)
	def makerepo():
		pass
	def dumpunreferenced():
		command('dumpunreferenced')
	def deleteunreferenced():
		command('deleteunreferenced')

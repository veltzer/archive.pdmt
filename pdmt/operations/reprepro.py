import operation

import pdmt.utils.subproc
import pdmt.config

"""
This module handles publishing and unpublishing a deb package from an apt repository

	Mark Veltzer <mark@veltzer.net>
"""
class Reprepro(operation.Operation):
	def run(self,nodes):
		args=[]
		if pdmt.config.ns_reprepro.p_sudo:
			args.append('sudo');
		args.append('reprepro');
		args.extend(['--basedir',pdmt.config.ns_reprepro.p_servicedir])
		args.extend(['--component',pdmt.config.ns_reprepro.p_component])
		args.extend(['includedeb',pdmt.config.ns_reprepro.p_codename,DEB])
		kw={}
		if pdmt.config.ns_reprepro.p_redirect:
			kw['stderr']=open('/dev/null')
			kw['stdout']=open('/dev/null')
		pdmt.utils.subproc.check_call(args,**kw)
	def remove():
		args=[]
		if pdmt.config.ns_reprepro.p_sudo:
			args.append('sudo');
		args.append('reprepro');
		args.extend(['--basedir',pdmt.config.ns_reprepro.p_servicedir])
		args.extend(['--component',pdmt.config.ns_reprepro.p_component])
		args.extend(['remove',pdmt.config.ns_reprepro.p_codename,NAME]);
		kw={}
		if pdmt.config.ns_reprepro.p_redirect:
			kw['stderr']=open('/dev/null')
			kw['stdout']=open('/dev/null')
		pdmt.utils.subproc.check_call(args,**kw)
	def command(name):
		args=[]
		if pdmt.config.ns_reprepro.p_sudo:
			args.append('sudo');
		args.append('reprepro');
		args.append(name);
		kw={}
		if pdmt.config.ns_reprepro.p_redirect:
			kw['stderr']=open('/dev/null')
			kw['stdout']=open('/dev/null')
		pdmt.utils.subproc.check_call(args,**kw)
	def makerepo():
		pass
	def dumpunreferenced():
		command('dumpunreferenced')
	def deleteunreferenced():
		command('deleteunreferenced');

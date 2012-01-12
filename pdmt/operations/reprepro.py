import operation

import subprocess
import pdmt.config
import config

"""
This module handles publishing and unpublishing a deb package from an apt repository

	Mark Veltzer <mark@veltzer.net>
"""
class Reprepro(operation.Operation):
	def run(self,nodes):
		args=[]
		if config.ns_reprepro.p_sudo:
			args.append('sudo');
		args.append('reprepro');
		args.extend(['--basedir',config.ns_reprepro.p_servicedir])
		args.extend(['--component',config.ns_reprepro.p_component])
		args.extend(['includedeb',config.ns_reprepro.p_codename,DEB])
		kw={}
		if config.ns_reprepro.p_redirect:
			kw['stderr']=open('/dev/null')
			kw['stdout']=open('/dev/null')
		subprocess.check_call(args,**kw)
	def remove():
		args=[]
		if config.ns_reprepro.p_sudo:
			args.append('sudo');
		args.append('reprepro');
		args.extend(['--basedir',config.ns_reprepro.p_servicedir])
		args.extend(['--component',config.ns_reprepro.p_component])
		args.extend(['remove',config.ns_reprepro.p_codename,NAME]);
		kw={}
		if config.ns_reprepro.p_redirect:
			kw['stderr']=open('/dev/null')
			kw['stdout']=open('/dev/null')
		subprocess.check_call(args,**kw)
	def command(name):
		args=[]
		if config.ns_reprepro.p_sudo:
			args.append('sudo');
		args.append('reprepro');
		args.append(name);
		kw={}
		if config.ns_reprepro.p_redirect:
			kw['stderr']=open('/dev/null')
			kw['stdout']=open('/dev/null')
		subprocess.check_call(args,**kw)
	def makerepo():
		pass
	def dumpunreferenced():
		command('dumpunreferenced')
	def deleteunreferenced():
		command('deleteunreferenced');

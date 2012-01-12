import operation

import pdmt.config
import config

import pdmt.utils.subproc
import os

"""
This operation knows how to make a debian package.
"""

class DebMaker(operation.Operation):
	def run(self,nodes):
		# check that everything is commited
		out=pdmt.utils.subproc.check_output(['git','status','-s'])
		if out!='':
			raise ValueError('first commit everything, then call me...')
		pdmt.utils.subproc.check_output(['python','setup.py','sdist'])
		name=config.ns_install.p_name+'-'+config.ns_install.p_version
		pdmt.utils.subproc.check_output(['py2dsc','dist/'+name+'.tar.gz'])
		# save the current directory
		cdir=os.getcwd()
		# change to 'deb_dist' and run 'debuild'
		os.chdir('deb_dist/'+name)
		pdmt.utils.subproc.system('debuild')
		# return to the current directory
		os.chdir(cdir)

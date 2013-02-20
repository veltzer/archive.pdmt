import operation

import pdmt.config

import pdmt.utils.subproc
import pdmt.utils.osw

"""
This operation knows how to make a debian package.
"""

class DebMaker(operation.Operation):
	def __init__(self):
		operation.Operation.__init__(
			self,
			'debmaker',
			'make a debian package',
		)
	def run(self,nodes):
		# check that everything is commited
		out=pdmt.utils.subproc.check_output(['git','status','-s'])
		if out!='':
			raise ValueError('first commit everything, then call me...')
		pdmt.utils.subproc.check_output(['python','setup.py','sdist'])
		name=pdmt.config.ns_product.p_name+'-'+pdmt.config.ns_product.p_version
		pdmt.utils.subproc.check_output(['py2dsc','dist/'+name+'.tar.gz'])
		# save the current directory
		cdir=pdmt.utils.osw.getcwd()
		# change to 'deb_dist' and run 'debuild'
		pdmt.utils.osw.chdir('deb_dist/'+name)
		pdmt.utils.subproc.check_call('debuild')
		# return to the current directory
		pdmt.utils.osw.chdir(cdir)

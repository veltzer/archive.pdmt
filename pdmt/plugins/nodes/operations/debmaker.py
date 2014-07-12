import pdmt.config
import pdmt.utils.subproc
import os # for chdir, getcwd

'''
This operation knows how to make a debian package.
'''

class Operation(object):
	def __init__(self):
		super().__init__(
			'debmaker',
			'make a debian package',
		)
	def run(self):
		# check that everything is commited
		out=pdmt.utils.subproc.check_output(['git','status','-s'])
		if out!='':
			raise ValueError('first commit everything, then call me...')
		pdmt.utils.subproc.check_output(['python','setup.py','sdist'])
		name=pdmt.config.ns_product.p_name+'-'+pdmt.config.ns_product.p_version
		pdmt.utils.subproc.check_output(['py2dsc','dist/'+name+'.tar.gz'])
		# save the current directory
		cdir=os.getcwd()
		# change to 'deb_dist' and run 'debuild'
		os.chdir('deb_dist/'+name)
		pdmt.utils.subproc.check_call('debuild')
		# return to the current directory
		os.chdir(cdir)

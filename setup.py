#!/usr/bin/python

import os # for chdir
import distutils.core # for setup
import subprocess # for check_output
import sys # for argv

##############
# parameters #
##############
check=True
debug=False

########
# code #
########
# this function is here because of python2.6 that does not have subprocess.check_output
def system_check_output(arg):
	pr=subprocess.Popen(arg,stdout=subprocess.PIPE)
	(output,errout)=pr.communicate()
	status=pr.returncode
	if status:
		raise ValueError('error in executing',arg)
	return output

if len(sys.argv)==2 and sys.argv[1]=='sdist':
	# check that everything is commited
	out=subprocess.check_output(['git','status','-s'])
	if check and out!='':
		raise ValueError('first commit everything, then call me...')

version=system_check_output(['git','describe']).rstrip()
if debug:
	print('version is ',version)
name='pdmt-'+version

dir_list=[]
for x in os.walk('pdmt'):
	dir_list.append(x[0])

distutils.core.setup(
	name='pdmt',
	description='Project Dependency Management Tool',
	author='Mark Veltzer',
	# this key is used for signing too
	author_email='mark@veltzer.net',
	url='http://veltzer.net/pdmt',
	version=version,
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: LGPL',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: Software Development :: Building',
	],
	requires=[
		'pygraph',
	],
	packages=dir_list,
	scripts=[
        ],
)
if sys.argv[1]=='sdist':
	subprocess.check_output(['py2dsc','dist/'+name+'.tar.gz'])
	# save the current directory
	cdir=os.getcwd()
	# change to 'deb_dist' and run 'debuild'
	os.chdir('deb_dist/'+name)
	os.system('debuild')
	# return to the current directory
	os.chdir(cdir)

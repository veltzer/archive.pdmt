#!/usr/bin/python

import os # for chdir
import distutils.core # for setup
import subprocess # for check_output

# check that everything is commited
out=subprocess.check_output(['git','status','-s'])
if out!='':
	raise ValueError('first commit everything, then call me...')
version=subprocess.check_output(['git','describe']),
name='pdmt-'+version

dir_list=[]
for x in os.walk('pdmt'):
	dir_list.append(x[0])

distutils.core.setup(
	name="pdmt",
	description="Project Dependency Management Tool",
	author="Mark Veltzer",
	# this key is used for signing too
	author_email="mark@veltzer.net",
	url="http://veltzer.net/pdmt",
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
		"pygraph",
	],
	packages=dir_list,
	scripts=[
        ],
)
subprocess.check_output(['py2dsc','dist/%s.tar.gz'.format(name=name)])
os.chdir('deb_dist/'+name)
os.system('debuild')

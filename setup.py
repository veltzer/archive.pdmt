#!/usr/bin/python3

'''
This is the installation tool. use minimal packages here.
dont use setuptools, dont use subprocess.
'''

import distutils.core # for setup

distutils.core.setup(
	name='pdmt',
	version='4',
	description='Project Dependency Management Tool (description)',
	long_description='Project Dependency Management Tool (long_description)',
	author='Mark Veltzer',
	author_email='mark.veltzer@gmail.com',
	maintainer='Mark Veltzer',
	maintainer_email='mark.veltzer@gmail.com',
	keywords=['make', 'pdmt', 'scons', 'build', 'tool'],
	url='https://veltzer.github.io/pdmt',
	license='LGPL',
	platforms=['ALL'],
	packages=['pdmt', 'pdmt/plugins', 'pdmt/plugins/eventhandlers', 'pdmt/plugins/nodehandlers', 'pdmt/plugins/nodes', 'pdmt/plugins/nodes/operations', 'pdmt/utils'],
	package_dir={'pdmt': 'src/pdmt',
	 'pdmt/plugins': 'src/pdmt/plugins',
	 'pdmt/plugins/eventhandlers': 'src/pdmt/plugins/eventhandlers',
	 'pdmt/plugins/nodehandlers': 'src/pdmt/plugins/nodehandlers',
	 'pdmt/plugins/nodes': 'src/pdmt/plugins/nodes',
	 'pdmt/plugins/nodes/operations': 'src/pdmt/plugins/nodes/operations',
	 'pdmt/utils': 'src/pdmt/utils'},
	classifiers=['Development Status :: 4 - Beta', 'Environment :: Console', 'Intended Audience :: Developers', 'License :: OSI Approved :: LGPL', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Topic :: Software Development :: Building', 'Topic :: Software Development :: Libraries', 'Topic :: Utilities'],
	data_files=[('/usr/bin', [])],
)

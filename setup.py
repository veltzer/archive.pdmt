#!/usr/bin/python3

import distutils.core # for setup
import setuptools # for find_packages
import subprocess # for check_output

distutils.core.setup(
	name='pdmt',
	description='Project Dependency Management Tool',
	long_description='Project Dependency Management Tool long description',
	author='Mark Veltzer',
	author_email='mark@veltzer.net',
	maintainer='Mark Veltzer',
	maintainer_email='mark@veltzer.net',
	keywords=[
		'make',
		'pdmt',
		'scons',
		'build',
		'tool',
	],
	url='https://www.veltzer.net/pdmt',
	license='LGPL',
	platforms=[
		'ALL',
	],
	#py_modules=[
	#	'pdmt',
	#],
	packages=setuptools.find_packages(),
	version=subprocess.check_output(['git','describe']).decode().rstrip(),
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: LGPL',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development :: Building',
		'Topic :: Software Development :: Libraries',
		'Topic :: Utilities',
	]
)

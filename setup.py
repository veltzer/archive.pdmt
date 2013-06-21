#!/usr/bin/python3

import distutils.core # for setup
#import setuptools # for find_packages

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
	url='http://www.veltzer.net',
	license='GPL',
	platforms='UNIX',
	version='2.2',
	requires=[],
	scripts=[],
	#py_modules=[
	#	'pdmt'
	#],
	#package_dir=pdmt.config.ns_product.p_package_dir,
	#packages=pdmt.config.ns_product.p_packages,
	#packages=setuptools.find_packages(),
	#namespace_packages=pdmt.config.ns_product.p_namespace_packages,
	data_files=[],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: LGPL',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: Software Development :: Building',
	]
)

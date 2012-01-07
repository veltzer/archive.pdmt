#!/usr/bin/python

import os
import distutils.core

dir_list=[]
for x in os.walk('core'):
	dir_list.append(x[0])

distutils.core.setup(
	name="pdmt",
	description="Project Dependency Management Tool",
	author="Mark Veltzer",
	author_email="mark.veltzer@gmail.com",
	url="http://veltzer.net/pdmt",
	version="1",
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

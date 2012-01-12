#!/usr/bin/python

import pdmt.config # for configuration
import distutils.core # for setup

distutils.core.setup(
	name=pdmt.config.ns_install.p_name,
	description=pdmt.config.ns_install.p_description,
	author=pdmt.config.ns_install.p_author,
	author_email=pdmt.config.ns_install.p_email,
	url=pdmt.config.ns_install.p_url,
	version=pdmt.config.ns_install.p_version,
	classifiers=pdmt.config.ns_install.p_classifiers,
	requires=pdmt.config.ns_install.p_require,
	packages=pdmt.config.ns_install.p_dir_list,
	scripts=pdmt.config.ns_install.p_scripts,
	data_files=pdmt.config.ns_install.p_data_files,
)

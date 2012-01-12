#!/usr/bin/python

import pdmt.config # for configuration
import distutils.core # for setup

distutils.core.setup(
	name=pdmt.config.ns_product.p_name,
	description=pdmt.config.ns_product.p_description,
	author=pdmt.config.ns_person.p_name,
	author_email=pdmt.config.ns_person.p_email,
	url=pdmt.config.ns_distrib.p_url_website,
	version=pdmt.config.ns_product.p_version,
	classifiers=pdmt.config.ns_product.p_classifiers,
	requires=pdmt.config.ns_product.p_require,
	packages=pdmt.config.ns_product.p_dir_list,
	scripts=pdmt.config.ns_product.p_scripts,
	data_files=pdmt.config.ns_product.p_data_files,
)

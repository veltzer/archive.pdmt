#!/usr/bin/python

import pdmt.config # for configuration
import distutils.core # for setup

distutils.core.setup(
	name=pdmt.config.ns_product.p_name,
	description=pdmt.config.ns_product.p_description,
	long_description=pdmt.config.ns_product.p_long_description,
	author=pdmt.config.ns_person.p_name,
	author_email=pdmt.config.ns_person.p_email,
	maintainer=pdmt.config.ns_person.p_name,
	maintainer_email=pdmt.config.ns_person.p_email,
	keywords=pdmt.config.ns_product.p_keywords,
	url=pdmt.config.ns_distrib.p_url_website,
	license=pdmt.config.ns_product.p_license,
	platforms=pdmt.config.ns_product.p_platforms,
	version=pdmt.config.ns_product.p_version,
	requires=pdmt.config.ns_product.p_requires,
	scripts=pdmt.config.ns_product.p_scripts,
	#py_modules=pdmt.config.ns_product.p_packages,
	#package_dir=pdmt.config.ns_product.p_package_dir,
	packages=pdmt.config.ns_product.p_packages,
	data_files=pdmt.config.ns_product.p_data_files,
	classifiers=pdmt.config.ns_product.p_classifiers,
)

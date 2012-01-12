#!/usr/bin/python

import config # for all parameters
import distutils.core # for setup

distutils.core.setup(
	name=config.ns_install.p_name,
	description=config.ns.install.p_description,
	author=config.ns_install.p_author,
	author_email=config.ns_insta.p_email,
	url=config.ns_install.p_url,
	version=config.ns_install.p_version,
	classifiers=config.ns_install.p_classifiers,
	requires=config.ns_install.p_require,
	packages=config.ns_install.p_dir_list,
)

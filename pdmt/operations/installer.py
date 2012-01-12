import operation

import pdmt.config
import config

import pdmt.utils.subproc

"""
This module installs dependencies for a package. Dependencies are gotten via
configuration
"""
class Installer(operation.Operation):
	def run(self,nodes):
		args=['sudo','apt-get','install']
		args.extend(config.ns_install.p_deps)
		pdmt.utils.subproc.check_call(args)

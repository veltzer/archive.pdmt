import operation

import pdmt.config

import pdmt.utils.subproc

"""
This module installs dependencies for a package. Dependencies are gotten via
configuration
"""
class DepsInstaller(operation.Operation):
	def run(self,nodes):
		args=['sudo','apt-get','install']
		args.extend(pdmt.config.ns_product.p_deps)
		pdmt.utils.subproc.check_call(args)

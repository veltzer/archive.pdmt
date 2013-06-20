import pdmt.operations.operation

import pdmt.config

import pdmt.utils.subproc

"""
This module installs dependencies for a package. Dependencies are gotten via
configuration
"""
class DepsInstaller(pdmt.operations.operation.Operation):
	def __init__(self):
		pdmt.operations.operation.Operation.__init__(
			self,
			'depsinstaller',
			'install prereqs',
		)
	def run(self,nodes):
		args=['sudo','apt-get','install']
		args.extend(pdmt.config.ns_product.p_deps)
		pdmt.utils.subproc.check_call(args)

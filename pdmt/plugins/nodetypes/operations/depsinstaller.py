import pdmt.api
import pdmt.config
import pdmt.utils.subproc

"""
This module installs dependencies for a package. Dependencies are gotten via
configuration
"""
class Operation(pdmt.api.Operation):
	def __init__(self):
		super().__init__(
			'depsinstaller',
			'install prereqs',
		)
	def run(self):
		args=['sudo','apt-get','install']
		args.extend(pdmt.config.ns_product.p_deps)
		pdmt.utils.subproc.check_call(args)

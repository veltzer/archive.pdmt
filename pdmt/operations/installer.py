import operation

import subprocess
import pdmt.config
import config

"""
This module installs dependencies for a package. Dependencies are gotten via
configuration
"""
class Installer(operation.Operation):
	def run(self,nodes):
		args=['sudo','apt-get','install']
		args.extend(config.ns_install.p_deps)
		subprocess.check_call(args)
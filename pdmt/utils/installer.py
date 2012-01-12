"""
This module installs dependencies for a package. Dependencies are gotten via
configuration
"""

import subprocess
import pdmt.config
import config

def doit():
	args=['sudo','apt-get','install']
	args.extend(config.ns_install.p_deps)
	subprocess.check_call(args)

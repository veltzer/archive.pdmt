import operation

import pdmt.config
import config

import os
import shutil
import subprocess

"""
In order for this plugin to work you have to make your web folder 
be writable by the user running pdmt.
You can do this with:
$ chmod g+w -R /var/www
$ chgrp $USER -R /var/www
"""

class InstallAptSite(operation.Operation):
	def __init__(self,p_name,p_description):
		super(InstallAptSite,self).__init__(p_name,p_description)
	def run(self,nodes):
		# the if is needed to avoid an exception
		serv=config.ns_reprepro.p_servicedir
		conf=os.path.join(serv,config.ns_reprepro.p_conf)
		if os.path.isdir(serv):
			shutil.rmtree(serv)
		os.mkdir(serv)
		os.mkdir(conf)
		shutil.copy('makot/distributions',conf)
		shutil.copy('makot/options',conf)
		shutil.copy('makot/index.php',serv)
		os.mkdir(os.path.join(serv,'pool'))
		subprocess.check_output([
			'gpg',
			'--armour',
			'--export',
			'--output',
			os.path.join(serv,config.ns_reprepro.p_keyname),
		])

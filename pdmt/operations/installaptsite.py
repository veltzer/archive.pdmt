import operation

import pdmt.config

import pdmt.utils.fileops
import pdmt.utils.subproc

import os

"""
In order for this plugin to work you have to make your web folder 
be writable by the user running pdmt.
You can do this with:
$ chmod g+w -R /var/www
$ chgrp $USER -R /var/www
"""

class InstallAptSite(operation.Operation):
	def run(self,nodes):
		# the if is needed to avoid an exception
		serv=pdmt.config.ns_reprepro.p_servicedir
		conf=os.path.join(serv,pdmt.config.ns_reprepro.p_conf)
		pdmt.utils.fileops.rmtreesoft(serv)
		pdmt.utils.fileops.mkdircopysoft('makot/distributions',conf)
		pdmt.utils.fileops.mkdircopysoft('makot/options',conf)
		pdmt.utils.fileops.mkdircopysoft('makot/index.php',serv)
		pdmt.utils.fileops.mkdir(os.path.join(serv,'pool'))
		pdmt.utils.subproc.check_output([
			'gpg',
			'--armour',
			'--export',
			'--output',
			os.path.join(serv,pdmt.config.ns_reprepro.p_keyname),
		])

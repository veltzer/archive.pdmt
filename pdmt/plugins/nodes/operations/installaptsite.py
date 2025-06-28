import os

import pdmt.config
import pdmt.utils.fileops
import pdmt.utils.subproc

'''
In order for this plugin to work you have to make your web folder 
be writable by the user running pdmt.
You can do this with:
$ chmod g+w -R /var/www
$ chgrp $USER -R /var/www
'''


class Operation:
    def __init__(self):
        super().__init__(
            'installaptsite',
            'install the apt site',
        )

    def run(self):
        # the if is needed to avoid an exception
        serv = pdmt.config.ns_apt.p_abs_dir
        conf = os.path.join(serv, pdmt.config.ns_apt.p_conf)
        pdmt.utils.fileops.rmtreesoft(serv)
        pdmt.utils.fileops.mkdircopysoft('makot/distributions', conf)
        pdmt.utils.fileops.mkdircopysoft('makot/options', conf)
        pdmt.utils.fileops.mkdircopysoft('makot/index.php', serv)
        # pdmt.utils.fileops.mkdir(os.path.join(serv,'pool'))
        final_key = os.path.join(serv, pdmt.config.ns_apt.p_keyname)
        pdmt.utils.subproc.check_output([
            'gpg',
            '--armour',
            '--export',
            '--output',
            final_key,
        ])
        pdmt.utils.fileops.chmod(final_key, 0o0444)
        # the creation of the next two files is so people could start using the site although
        # it is empty
        pdmt.utils.fileops.create_empty_filegz(pdmt.config.ns_apt.p_file_sources)
        pdmt.utils.fileops.create_empty_file(pdmt.config.ns_apt.p_file_binary)

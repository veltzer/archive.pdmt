import imp
import os.path

if os.path.isfile('pdmt/cfg.py'):
    imp.load_source('pdmt.config', 'pdmt/cfg.py')
else:
    deb_file = '/usr/lib/python3/dist-packages/pdmt/cfg.py'
    if os.path.isfile(deb_file):
        imp.load_source('pdmt.config', deb_file)

overridefiles = os.path.expanduser('~/.cfg.py')
if os.path.isfile(overridefiles):
    imp.load_source('pdmt.config', overridefiles)


def show():
    for ns_name in pdmt.config.__dict__:
        # if not ns_name.startswith('__'):
        if ns_name.startswith('ns_'):
            print(ns_name)
            ns = pdmt.config.__dict__[ns_name]
            for p in ns.__dict__:
                # if not p.startswith('__'):
                if p.startswith('p_'):
                    print('\t', p, ns.__dict__[p])

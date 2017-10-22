"""
project definitions for pdmt
"""

import templar.utils


def populate(d):
    # project section
    d.project_github_username = 'veltzer'
    d.project_name = 'pdmt'
    d.project_website = 'https://{project_github_username}.github.io/{project_name}'.format(**d)
    d.project_website_source = 'https://github.com/{project_github_username}/{project_name}'.format(**d)
    d.project_website_git = 'git://github.com/{project_github_username}/{project_name}.git'.format(**d)
    d.project_website_download = 'https://launchpad.net/~mark-veltzer/+archive/ubuntu/ppa'
    d.project_paypal_donate_button_id = 'XKSSBRVJM7HHA'
    d.project_google_analytics_tracking_id = 'UA-56436979-1'

    d.project_short_description = 'Project Dependency Management Tool (short_description)'
    d.project_description = 'Project Dependency Management Tool (description)'
    d.project_long_description = 'Project Dependency Management Tool (long_description)'
    d.project_md_description = '''* pdmt is influenced by scons but also very different from scons.
* pdmt usage is regular python. Pdmt is a python library first.
* extending pdmt requires python knowledge and oo knowledge.
* pdmt has a command line interface.
* pdmt can be used for continuous builds as it can watch files for changes.
* pdmt doesnt just work on files. It can work on records from databases too.
It can watch remote urls.
It has dependency on configuration as well.'''.format(**d)
    d.project_year_started = '2010'
    d.project_keywords = [
        'make',
        'pdmt',
        'scons',
        'build',
        'tool',
    ]
    d.project_platforms = [
        'ALL',
    ]
    d.project_license = 'LGPL'
    d.project_classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Building',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ]
    d.project_data_files = []
    # d.project_data_files.append(templar.utils.hlp_files_under('/usr/bin', 'src/*'))

    d.project_prereqs = [
        # curses and text gui
        'python3-progressbar',
        'python-progressbar',

        # packages needed to build .debs from python code
        'devscripts',
        'python-pydot',  # for dot graph generation
        'python-all-dev',
        'python-stdeb',
        'build-essential',
        'dpkg-dev',
        'debhelper',
        'fakeroot',
        'cdbs',
        'git-buildpackage',

        # docbook stuff
        'docbook5-xml',
        'docbook-xsl-ns',
        'docbook-defguide',
        'xsltproc',
        'fop',
        'xmlto',
        'libxml2-utils',
        'xmlstarlet',
        'pandoc',

        # cmd2 stuff
        'python3-cmd2',
        'python-cmd2',

        # inotify
        'python-pyinotify',
        'python3-pyinotify',
        'python-pyinotify-doc',

        # graph
        'python3-pygraph',
        'python-pygraph',
        'python-igraph',

        # profiling
        'python3-objgraph',
        'python-objgraph',
        'python-objgraph-doc',
        'python3-memprof',
        'python-memprof',
        'python3-psutil',
        'python-psutil',

        # other tools
        'scons',
        # 'gradle',
        'maven',

        # my own
        'templar',
    ]

    # deb section
    d.deb_package = True
    d.deb_section = 'python'
    d.deb_priority = 'optional'
    d.deb_architecture = 'all'
    d.deb_pkgname = 'pdmt'
    # to which series to publish the package?
    d.deb_series = [
        'artful',
        'zesty',
        'xenial',
        'trusty',
    ]
    d.deb_depends = '${misc:Depends}, ${python3:Depends}, python3-mako'
    d.deb_builddepends = 'python3, python3-setuptools, debhelper, dh-python'
    d.deb_standards_version = '3.9.8'
    d.deb_x_python_version = '>= 3.4'
    d.deb_x_python3_version = '>= 3.4'
    d.deb_urgency = 'low'
    d.entry_points = {
        'console_scripts': [
        ],
    }


def get_deps():
    return [
        __file__,  # myself
    ]

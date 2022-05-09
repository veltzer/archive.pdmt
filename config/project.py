project_github_username = "veltzer"
project_name = "pdmt"
project_website = f"https://{project_github_username}.github.io/{project_name}"
project_website_source = f"https://github.com/{project_github_username}/{project_name}"
project_website_git = f"git://github.com/{project_github_username}/{project_name}.git"
project_website_download = "https://launchpad.net/~mark-veltzer/+archive/ubuntu/ppa"
project_paypal_donate_button_id = "XKSSBRVJM7HHA"
project_google_analytics_tracking_id = "UA-56436979-1"

project_short_description = "Project Dependency Management Tool (short_description)"
project_description = "Project Dependency Management Tool (description)"
project_long_description = "Project Dependency Management Tool (long_description)"
project_md_description = f"""* pdmt is influenced by scons but also very different from scons.
* pdmt usage is regular python. Pdmt is a python library first.
* extending pdmt requires python knowledge and oo knowledge.
* pdmt has a command line interface.
* pdmt can be used for continuous builds as it can watch files for changes.
* pdmt doesnt just work on files. It can work on records from databases too.
It can watch remote urls.
It has dependency on configuration as well."""
project_year_started = 2010
project_keywords = [
    "make",
    "pdmt",
    "scons",
    "build",
    "tool",
]
project_platforms = [
    "ALL",
]
project_license = "LGPL"
project_classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: LGPL",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Building",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]
project_data_files = []
# project_data_files.append(templar.utils.hlp_files_under("/usr/bin", "src/*"))

project_prereqs = [
    # curses and text gui
    "python3-progressbar",
    "python-progressbar",

    # packages needed to build .debs from python code
    "devscripts",
    "python-pydot",  # for dot graph generation
    "python-all-dev",
    "python-stdeb",
    "build-essential",
    "dpkg-dev",
    "debhelper",
    "fakeroot",
    "cdbs",
    "git-buildpackage",

    # docbook stuff
    "docbook5-xml",
    "docbook-xsl-ns",
    "docbook-defguide",
    "xsltproc",
    "fop",
    "xmlto",
    "libxml2-utils",
    "xmlstarlet",
    "pandoc",

    # cmd2 stuff
    "python3-cmd2",
    "python-cmd2",

    # inotify
    "python-pyinotify",
    "python3-pyinotify",
    "python-pyinotify-doc",

    # graph
    "python3-pygraph",
    "python-pygraph",
    "python-igraph",

    # profiling
    "python3-objgraph",
    "python-objgraph",
    "python-objgraph-doc",
    "python3-memprof",
    "python-memprof",
    "python3-psutil",
    "python-psutil",

    # other tools
    "scons",
    # "gradle",
    "maven",

    # my own
    "templar",
]

# deb section
deb_package = True
deb_section = "python"
deb_priority = "optional"
deb_architecture = "all"
deb_pkgname = "pdmt"
# to which series to publish the package?
deb_series = [
    "artful",
    "zesty",
    "xenial",
    "trusty",
]
deb_depends = "${misc:Depends}, ${python3:Depends}, python3-mako"
deb_builddepends = "python3, python3-setuptools, debhelper, dh-python"
deb_standards_version = "3.9.8"
deb_x_python_version = ">= 3.4"
deb_x_python3_version = ">= 3.4"
deb_urgency = "low"
entry_points = {
    "console_scripts": [
    ],
}
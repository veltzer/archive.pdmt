'''
project definitions for templar
'''

def populate(d):
	# project section
	d.project_name='pdmt'
	d.project_long_description='Project Dependency Management Tool'
	d.project_year_started='2010'
	d.project_description='''* pdmt is influenced by scons but also very different from scons.
* pdmt usage is regular python. Pdmt is a python library first.
* extending pdmt requires python knowledge and oo knowledge.
* pdmt has a command line interface.
* pdmt can be used for continuous builds as it can watch files for changes.
* pdmt doesn't just work on files. It can work on records from databases too.
It can watch remote urls.
It has dependency on configuration as well.'''.format(**d)

	# deb section
	d.deb_pkg_name='pdmt'
	d.deb_urgency='low'

def getdeps():
	return [
		__file__, # myself
	]

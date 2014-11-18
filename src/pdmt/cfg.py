# do not import any pdmt classes here except boot
# you may use other classes as long as they are supported in all versions
# of python you will be using
import pdmt.utils.boot

class ns_pdmt:
	try:
		p_version=pdmt.utils.boot.system_check_output(['git','describe']).rstrip()
	except:
		p_version='0'
class ns_product:
	p_license='GPL'
	p_name='pdmt'
	try:
		p_version=pdmt.utils.boot.system_check_output(['git','describe']).rstrip()
	except:
		p_version='0'
	p_description='Project Dependency Management Tool'
	p_long_description='Project Dependency Management Tool long description'
	p_keywords=[
		'make',
		'pdmt',
		'scons',
		'build',
		'tool',
	]
	p_platforms='UNIX'
	# source code package where the code is
	p_package='pdmt'
	p_packages=[ 'pdmt' ]
	p_namespace_packages=[ 'pdmt' ]
	#pdmt.utils.boot.dir_list(p_package)
	p_package_dir={
		'pdmt':'pdmt',
	}
	p_deps=[
	#	'python-pygraph',
	#	'python-pyinotify',
	#	'python-pyinotify-doc',
	#	'python-inotifyx',
	#	'python-stdeb',
	#	'python-pygraphviz',
	#	'libgv-python',
	]
	p_requires=[
	#	'pygraph',
	]
	p_classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: LGPL',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: Software Development :: Building',
	]
	p_scripts=[
	]
	p_data_files=[
	]
	p_cannonical='python-'+p_name
# person related parameters
class ns_person:
	p_name='Mark Veltzer'
	# this key is used for signing...
	p_email='mark@veltzer.net'
	p_keyid='6752126F'
	p_fullname=p_name+' <'+p_email+'>'
# distribution related parameters
class ns_distrib:
	p_domain=pdmt.utils.boot.system_check_output(['hostname','--domain']).rstrip()
	p_url_website='http://'+p_domain+'/'+ns_product.p_name
# apt distribution parameters
class ns_apt:
	p_rel_dir='apt'
	p_abs_dir='/var/www/'+p_rel_dir
	p_url='http://'+ns_distrib.p_domain+'/'+p_rel_dir
	p_deb_file='deb_dist/'+ns_product.p_cannonical+'_'+ns_product.p_version+'-1_all.deb'
	p_sudo=False
	p_conf='conf'
	p_component='main'
	p_components='main'
	p_codename=pdmt.utils.boot.system_check_output(['lsb_release','--codename','--short']).rstrip()
	p_id=pdmt.utils.boot.system_check_output(['lsb_release','--id','-s']).rstrip()
	p_keyname='public_key.gpg'
	p_architectures='i386 source'
	p_file_sources=os.path.join(p_abs_dir,'dists',p_codename,p_component,'source','Sources.gz')
	p_file_binary=os.path.join(p_abs_dir,'dists',p_codename,p_component,'binary-i386','Packages')
class ns_chandler:
	p_sourcefilesuffix='.c'
	p_objectfilesuffix='.o'
class ns_makohandler:
	p_sourcefilesuffix='.mako'
	p_targetdir='makot'
class ns_fileops:
	p_debug=True
	p_debug=False
	p_print=False
class ns_subproc:
	p_debug=True
	p_debug=False
class ns_mgr:
	p_prog=False
	p_dbg=False
class ns_release:
	p_email=False
	p_tweet=True
	p_subject='A new version of '+ns_product.p_name+' is out'
	p_from=ns_product.p_name+' author: '+ns_person.p_name
	p_to=[
		ns_person.p_email,
		'shay@hinbit.com',
	]
	p_smtp_host='smtp.gmail.com'
	p_content='Check out the new version of '+ns_product.p_name+' in '+ns_distrib.p_url_website
	#p_mail_user=[mail_user]
	#p_mail_password=[mail_password]
	#p_twitter_user=[twitter_user]
	#p_twitter_password=[twitter_password]
	p_debug=False
	p_usetls=True

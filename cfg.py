import os
import subprocess

# this function is here because of python2.6 that does not have subprocess.check_output
def system_check_output(arg):
	pr=subprocess.Popen(arg,stdout=subprocess.PIPE)
	(output,errout)=pr.communicate()
	status=pr.returncode
	if status:
		raise ValueError('error in executing',arg)
	return output

class ns_release:
	p_email=True
	p_tweet=False
	p_subject='A new version of optimus is out'
	p_from='Optimus release manager: Mark Veltzer'
	p_to='mark.veltzer@gmail.com,shay@hinbit.com'
	p_smtp_host='smtp.gmail.com'
	p_content='Check out the new version of optimus in http://www.veltzer.net/optimus'
	#p_mail_user=[mail_user]
	#p_mail_password=[mail_password]
	#p_twitter_user=[twitter_user]
	#p_twitter_password=[twitter_password]
	p_debug=True
	p_usetls=True
class ns_install:
	p_name='pdmt'
	p_description='Project Dependency Management Tool'
	p_author='Mark Veltzer'
	# this key is used for signing...
	p_email='mark@veltzer.net'
	p_dir_list=[]
	for x in os.walk('pdmt'):
		p_dir_list.append(x[0])
	p_deps=[
		'python-pygraph',
		'python-pyinotify',
		'python-pyinotify-doc',
		'python-inotifyx',
		'python-stdeb',
	]
	p_require=[
		'pygraph',
	]
	p_version=system_check_output(['git','describe']).rstrip()
	p_url='http://veltzer.net/pdmt'
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
		'cfg.py',
	]

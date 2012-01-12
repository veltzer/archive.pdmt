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
	p_deps=[
		'python-pygraph',
		'python-pyinotify',
		'python-pyinotify-doc',
		'python-inotifyx',
		'python-stdeb',
	]

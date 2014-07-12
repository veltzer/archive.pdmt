'''
This is a module which should never use pdmt classes. It is intended to aid in the
writing of the pdmt config

It intentionaly will duplicate code in other utils since it is a boot strapper.
'''

import subprocess
import os

# this function is here because python2.6 does not have subprocess.check_output
def system_check_output(arg):
	pr=subprocess.Popen(arg,stdout=subprocess.PIPE)
	(output,errout)=pr.communicate()
	status=pr.returncode
	if status:
		raise ValueError('error in executing',arg)
	return str(output)
def dir_list(arg):
	p_dir_list=[]
	for x in os.walk(arg):
		p_dir_list.append(x[0])
	return p_dir_list

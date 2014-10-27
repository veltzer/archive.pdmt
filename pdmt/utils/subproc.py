'''
This module helps in running two commands with a pipe between them.

	Mark Veltzer <mark@veltzer.net>
'''

'''
This function receives two lists to serve as the new processes
'''
import subprocess
import sys

import pdmt.config

def debug(msg):
	if pdmt.config.ns_subproc.p_debug:
		print(msg)
def system_pipe(list1,list2,out):
	debug('system_pipe ['+str(list1)+','+str(list2)+','+str(out)+']')
	pr1=subprocess.Popen(
		list1,
		stdout=subprocess.PIPE,
	)
	pr2=subprocess.Popen(
		list2,
		stdin=pr1.stdout,
		stdout=out,
	)
	# the order of the following two lines don't matter but we do need
	# to wait for the two processes to be over...
	status=pr1.wait()
	if status:
		raise ValueError('error in executing',list1)
	status=pr2.wait()
	status=pr2.returncode
	if status:
		raise ValueError('error in executing',list2)
# this function is here because of python2.6 that does not have subprocess.check_output
def system_check_output(arg):
	pr=subprocess.Popen(arg,stdout=subprocess.PIPE)
	(output,errout)=pr.communicate()
	status=pr.returncode
	if status:
		raise ValueError('error in executing',arg)
	return output
def check_output(arg,**kw):
	debug('check_output ['+str(arg)+']')
	return subprocess.check_output(arg,**kw)
def check_call(arg,**kw):
	debug('check_call ['+str(arg)+']')
	subprocess.check_call(arg,**kw)
def system_list(args,**kw):
	debug('system_list ['+str(args)+']')
	pr=subprocess.Popen(args,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(output,errout)=pr.communicate()
	return (pr.returncode, output.decode(), errout.decode())
def system_string(s):
	debug('system ['+str(s)+']')
	pr=subprocess.Popen(s,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	(output,errout)=pr.communicate()
	return (pr.returncode, output.decode(), errout.decode())

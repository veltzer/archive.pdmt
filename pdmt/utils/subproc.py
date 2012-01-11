"""
This module helps in running two commands with a pipe between them.

	Mark Veltzer <mark@veltzer.net>
"""

"""
This function receives two lists to serve as the new processes
"""
import subprocess
import sys
def system_pipe(list1,list2,out=None):
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

if __name__=='__main__':
	try:
		# test error in first command
		system_pipe(
			['ls','-l','foo'],
			['wc','-l'],
		);
	except ValueError,e:
		print('ok, got error for first command',e)
	try:
		# test error in second command
		system_pipe(
			['ls','-l'],
			['wc','-l','--stam'],
		);
	except ValueError,e:
		print('ok, got error for second command',e)
	# test output
	system_pipe(
		['ls','-l'],
		['wc','-l'],
		out=open('/dev/null','w'),
	);

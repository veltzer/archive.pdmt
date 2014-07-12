'''
The idea of this package is that all file operations will go through here
If this will be the case then it will be very easy to debug all file operations.
'''

import pdmt.config # for ns_fileops
import shutil # for rmtree, copy
import os # for unlink, mkdir, chmod
import os.path # for isdir, dirname, split
import gzip # for open
import pdmt.utils.printer # for print_msg

def debug(msg):
	if pdmt.config.ns_fileops.p_debug:
		print(msg)
def print_msg(msg):
	if pdmt.config.ns_fileops.p_print:
		pdmt.utils.printer.print_msg('unlinking [{name}]'.format(name=p_file))
def rmtree(p_dir):
	debug('rmtree ['+p_dir+']')
	shutil.rmtree(p_dir)
def rmtreesoft(p_dir):
	debug('rmtreesoft ['+p_dir+']')
	if os.path.isdir(p_dir):
		shutil.rmtree(p_dir)
def copy(p_file,p_dir):
	debug('copy ['+p_file+','+p_dir+']')
	shutil.copy(p_file,p_dir)
def unlink(p_file):
	print_msg('unlinking [{name}]'.format(name=p_file))
	debug('unlink ['+p_file+']')
	os.unlink(p_file)
def unlinksoft(p_file):
	debug('unlinksoft ['+p_file+']')
	if os.path.isfile(p_file):
		print_msg('unlinksoft [{name}] (really)'.format(name=p_file))
		os.unlink(p_file)
	else:
		print_msg('unlinksoft [{name}] (notthere)'.format(name=p_file))
def mkdir(p_dir):
	debug('mkdir ['+p_dir+']')
	os.mkdir(p_dir)
def mkdirparent(p_dir):
	debug('mkdirparent ['+p_dir+']')
	to_create=[]
	while not os.path.isdir(p_dir) and not p_dir=='':
		to_create.append(p_dir)
		p_dir=os.path.dirname(p_dir)
	for directory in reversed(to_create):
		os.mkdir(directory)
def mkdirparent_file(p_file):
	debug('mkdirparent_file ['+p_file+']')
	p_dir=os.path.dirname(p_file)
	mkdirparent(p_dir)
def mkdircopysoft(p_file,p_dir):
	debug('mkdircopysoft ['+p_file+','+p_dir+']')
	mkdirparent(p_dir)
	shutil.copy(p_file,p_dir)
def chmod(p_file,p_mode):
	debug('chmod ['+p_file+','+str(p_mode)+']')
	os.chmod(p_file,p_mode)
def create_empty_file(p_file):
	debug('create_empty_file ['+p_file+']')
	mkdirparent(os.path.split(p_file)[0])
	f=open(p_file,'w')
	f.close()
def create_empty_filegz(p_file):
	debug('create_empty_filegz ['+p_file+']')
	mkdirparent(os.path.split(p_file)[0])
	f=gzip.open(p_file,'w')
	f.close()

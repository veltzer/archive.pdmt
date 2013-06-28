"""
The idea of this package is that all file operations will go through here
If this will be the case then it will be very easy to debug all file operations.
"""
import pdmt.config

import shutil
import os
import gzip

def debug(msg):
	if pdmt.config.ns_fileops.p_debug:
		print(msg)
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
	debug('unlink ['+p_file+']')
	os.unlink(p_file)
def unlinksoft(p_file):
	debug('unlinksoft ['+p_file+']')
	try:
		os.unlink(p_file)
	except:
		pass
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

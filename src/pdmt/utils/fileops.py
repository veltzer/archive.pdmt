'''
The idea of this package is that all file operations will go through here
If this will be the case then it will be very easy to debug all file operations.
'''

import pdmt.config # for ns_fileops
import shutil # for rmtree, copy
import os # for unlink, mkdir, chmod, stat
import stat # for S_IWUSR, S_IWGRP, S_IWOTH
import os.path # for isdir, dirname, split, getmtime
import gzip # for open
import pdmt.utils.printer # for print_msg

doCache=False

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
def unlinksoft_nocache(p_file):
    debug('unlinksoft ['+p_file+']')
    if os.path.isfile(p_file):
        print_msg('unlinksoft [{name}] (really)'.format(name=p_file))
        os.unlink(p_file)
    else:
        print_msg('unlinksoft [{name}] (notthere)'.format(name=p_file))
files=dict()
def unlinksoft_cache(filename):
    global files
    if filename not in files:
        if os.path.isfile(filename):
            print_msg('unlinksoft [{name}] (really)'.format(name=filename))
            os.unlink(filename)
            files[filename]=False
        else:
            print_msg('unlinksoft [{name}] (notthere)'.format(name=filename))
            files[filename]=False
    else:
        if files[filename]==True:
            print_msg('unlinksoft [{name}] (really)'.format(name=filename))
            os.unlink(filename)
            files[filename]=False
        else:
            print_msg('unlinksoft [{name}] (notthere)'.format(name=filename))
def checkexist_and_updatecache(filename):
    global files, mtimes
    if not os.path.isfile(filename):
        raise ValueError('do not have file after build', filename)
    if doCache:
        files[filename]=True
        mtimes[filename]=os.path.getmtime(filename)
def mkdir(p_dir):
    debug('mkdir ['+p_dir+']')
    os.mkdir(p_dir)
''' create all the folders necessary for a file '''
def mkdirp(p_file):
    dir=os.path.dirname(p_file)
    if not os.path.isdir(dir):
        os.makedirs(dir)
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
def chmod_mw(p_file):
    mode=os.stat(p_file).st_mode
    os.chmod(p_file, mode & ~(stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))
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
mtimes=dict()
def getmtime_cache(filename):
    if filename in mtimes:
        return mtimes[filename]
    else:
        ret=os.path.getmtime(filename)
        mtimes[filename]=ret
        return ret
def getmtime_nocache(filename):
    return os.path.getmtime(filename)

########################
# handle cache/nocache #
########################
if doCache:
    unlinksoft=unlinksoft_cache
    getmtime=getmtime_cache
else:
    unlinksoft=unlinksoft_nocache
    getmtime=getmtime_nocache

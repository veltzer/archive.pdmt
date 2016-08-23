'''
This is a module which should never use pdmt classes. It is intended to aid in the
writing of the pdmt config

It intentionaly will duplicate code in other utils since it is a boot strapper.
'''

import subprocess # for Popen, PIPE, DEVNULL
import os # for walk

def system_check_output(arg):
    pr=subprocess.Popen(arg,stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    (output,errout)=pr.communicate()
    status=pr.returncode
    if status:
        raise ValueError('error in executing',arg)
    return output.decode()

def dir_list(arg):
    p_dir_list=[]
    for x in os.walk(arg):
        p_dir_list.append(x[0])
    return p_dir_list

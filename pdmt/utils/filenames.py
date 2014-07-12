'''
This package handles file name manipulations
'''

import os.path # for join, basename

''' remove the suffix from the original file and replace it with the new suffix. return the result '''
def replace_suffix(orig, suffix):
	return orig[:orig.rfind('.')]+suffix

def replace_suffix_new_folder(orig, suffix, folder):
	return os.path.join(folder, os.path.basename(replace_suffix(orig, suffix)))

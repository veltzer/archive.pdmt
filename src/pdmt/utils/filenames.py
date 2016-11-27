"""
This package handles file name manipulations
"""

import os.path


def replace_suffix(orig, suffix):
    """ remove the suffix from the original file and replace it with the new suffix. return the result """
    return orig[:orig.rfind('.')]+suffix


def replace_suffix_new_folder(orig, suffix, folder):
    return os.path.join(folder, os.path.basename(replace_suffix(orig, suffix)))

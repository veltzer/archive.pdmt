"""
This is a collection of string utilities that we may need in pdmt
"""


def common_prefix(a, b):
    """
    a function to find the longest common prefix
    between two strings. Could be used for command line
    completion and the like
    """
    for i, s in enumerate(a):
        if a[i] != b[i]:
            break
    else:
        return a
    return a[:i]

"""
language utilities are a bunch of functions which know how
to do natural language stuff.
This makes talking to the user nicer
"""


def plural(name, num):
    """
    A function that knows how to do plural in the english language
    """
    if num > 1 or num == 0:
        name += 's'
    return name


def bool_to_ok(b):
    if b:
        return 'FAIL'
    else:
        return 'OK'

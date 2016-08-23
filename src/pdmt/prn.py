'''
prn==Pdmt Resource name
pdmt resource mgmt utils
'''

def create(name=None, proto=None):
    return '{proto}://{name}'.format(
        proto=proto,
        name=name
    )

def get_name_from_prn(s):
    raise ValueError('implement me')
def get_proto_from_prn(s):
    raise ValueError('implement me')
def get_name_proto_from_prn(s):
    raise ValueError('implement me')

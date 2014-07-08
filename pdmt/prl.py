'''
pdmt resource mgmt utils
'''

def create(name=None, proto=None):
	return '{proto}://{name}'.format(
		proto=proto,
		name=name
	)

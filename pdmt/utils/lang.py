'''
language utilities are a bunch of functions which know how
to do natural language stuff.
This makes talking to the user nicer
'''

'''
A function that knows how to do plural in the english language
'''
def plural(name, num):
	if num>1 or num==0:
		name+='s'
	return name

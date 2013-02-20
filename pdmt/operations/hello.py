import operation

"""
A simple hello world operation (prints hello world on the screen)
"""

class Hello(operation.Operation):
	def __init__(self):
		operation.Operation.__init__(
			self,
			"hello",
			"print hello on the screen",
		)
	def run(self,nodes):
		print "Hello, World!\n";

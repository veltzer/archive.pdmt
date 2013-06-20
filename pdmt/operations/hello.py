import pdmt.operations.operation

"""
A simple hello world operation (prints hello world on the screen)
"""

class Hello(pdmt.operations.operation.Operation):
	def __init__(self):
		pdmt.operations.operation.Operation.__init__(
			self,
			"hello",
			"print hello on the screen",
		)
	def run(self,nodes):
		print("Hello, World!\n");

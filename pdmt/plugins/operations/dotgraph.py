import pdmt.api

"""
A simple hello world operation (prints hello world on the screen)
"""

class Operation(pdmt.api.Operation):
	def __init__(self):
		super().__init__(
			'hello',
			'print hello on the screen',
		)
	def run(self):
		mgr.dotgraph()

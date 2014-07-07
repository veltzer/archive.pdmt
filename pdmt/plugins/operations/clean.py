import pdmt.api

"""
A generic clean node for Pdmt
"""

class Operation(pdmt.api.Operation):
	def __init__(self):
		super().__init__(
			'hello',
			'print hello on the screen',
		)
	def run(self):
		lst_len=self.graph.get_nodes_num()
		self.progress('going to clean '+str(lst_len)+' '+pdmt.utils.lang.plural('node', lst_len))
		for node in self.graph.get_nodes():
			self.debug(node)
			node.clean()

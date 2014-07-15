import pdmt.plugins.nodes.operation # for NodeType

'''
An operation to print the graph in dot notation
'''

class NodeType(pdmt.plugins.nodes.operation.NodeType):
	def __init__(self, **kw):
		super().__init__(name='print_dot', description='print graph in dot notation', **kw)
	def build(self):
		self.mgr.print_dot()

import pdmt.plugins.nodes.operation # for NodeType

'''
An operation to print the graph in dot notation
'''

class NodeType(pdmt.plugins.nodes.operation.NodeType):
	def __init__(self, name=None):
		super().__init__(name='print_dot', description='print graph in dot notation')
	def build(self):
		self.mgr.graph.print_dot()

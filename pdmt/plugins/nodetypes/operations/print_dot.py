import pdmt.plugins.nodetypes.operation # for NodeType

"""
An operation to print the graph in dot notation
"""

class NodeType(pdmt.plugins.nodetypes.operation.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name='print_dot', proto=proto)
		self.description='print graph in dot notation'
	def build(self):
		self.mgr.graph.print_dot()

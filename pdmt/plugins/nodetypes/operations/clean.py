import pdmt.plugins.nodetypes.operation # for NodeType
import pdmt.utils.lang # for plural

"""
A generic clean node for Pdmt
"""

class NodeType(pdmt.plugins.nodetypes.operation.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name='clean', proto=proto)
		self.description='clean all nodes'
	def build(self):
		lst_len=self.mgr.graph.get_node_num()
		self.mgr.progress('going to clean [{lst_len}] {plural}...'.format(
			lst_len=lst_len,
			plural=pdmt.utils.lang.plural('node', lst_len),
		))
		for node in self.mgr.graph.get_nodes():
			node.clean()

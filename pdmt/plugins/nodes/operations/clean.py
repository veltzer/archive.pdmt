import pdmt.plugins.nodes.operation # for NodeType
import pdmt.utils.lang # for plural
import pdmt.utils.printer # for print_msg

'''
A generic clean node for Pdmt
'''

class NodeType(pdmt.plugins.nodes.operation.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name='clean', proto=proto)
		self.description='clean all nodes'
	def build(self):
		lst_len=self.mgr.graph.get_node_num()
		self.mgr.progress('going to clean [{lst_len}] {plural}...'.format(
			lst_len=lst_len,
			plural=pdmt.utils.lang.plural('node', lst_len),
		))
		for i,node in enumerate(self.mgr.graph.get_nodes()):
			pdmt.utils.printer.print_msg('cleaning ({num}/{len_todo}) [{name}]'.format(
				num=i+1,
				len_todo=lst_len,
				name=node.get_name(),
			))
			node.clean()

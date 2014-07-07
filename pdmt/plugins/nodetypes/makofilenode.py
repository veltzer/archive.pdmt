import pdmt.plugins.nodetypes.sourcefilenode
import pdmt.types # for t_mako

"""
This node represents a mako source file
"""

class NodeType(pdmt.plugins.nodetypes.sourcefilenode.NodeType):
	def __init__(self,name):
		super().__init__(name=name,type=pdmt.types.t_mako)

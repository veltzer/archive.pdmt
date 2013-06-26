import pdmt.nodetypes.sourcefilenode
import pdmt.types

"""
This node represents C source code
"""

class NodeType(pdmt.nodetypes.sourcefilenode.NodeType):
	def __init__(self,fname):
		super().__init__(fname,pdmt.types.t_c)

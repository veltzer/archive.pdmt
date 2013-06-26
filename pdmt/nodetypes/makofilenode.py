import pdmt.nodetypes.sourcefilenode
import pdmt.types

"""
This node represents a mako source file
"""

class NodeType(pdmt.nodetypes.sourcefilenode.NodeType):
	def __init__(self,p_fname):
		super().__init__(p_fname,pdmt.types.t_mako)

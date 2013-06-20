import pdmt.nodetypes.sourcefilenode
import pdmt.types

"""
This node represents a mako source file
"""

class MakoFileNode(pdmt.nodetypes.sourcefilenode.SourceFileNode):
	def __init__(self,p_fname):
		super(MakoFileNode,self).__init__(p_fname,pdmt.types.t_mako)

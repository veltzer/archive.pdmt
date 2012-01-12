import sourcefilenode
import pdmt.types

"""
This node represents a mako source file
"""

class MakoFileNode(sourcefilenode.SourceFileNode):
	def __init__(self,p_fname):
		super(MakoFileNode,self).__init__(p_fname,pdmt.types.t_mako)

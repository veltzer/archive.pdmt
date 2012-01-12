import sourcefilenode
import pdmt.types

"""
This node represents a mako source file
"""

class MakoFileNode(sourcefilenode.SourceFileNode):
	def __init__(self,fname):
		super(MakoFileNode,self).__init__(fname,pdmt.types.t_mako)

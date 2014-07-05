import pdmt.plugins.nodetypes.sourcefilenode
import pdmt.types

"""
This is an unknown file node.
Why would you need it?
When you don't know what it is that you are producing (check for instance
the mako module).
"""

class NodeType(pdmt.plugins.nodetypes.sourcefilenode.NodeType):
	def __init__(self,fname):
		super().__init__(fname,pdmt.types.t_unknown)

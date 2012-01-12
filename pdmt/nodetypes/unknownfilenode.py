import sourcefilenode
import pdmt.types

"""
This is an unknown file node.
Why would you need it?
When you don't know what it is that you are producing (check for instance
the mako module).
"""

class UnknownFileNode(sourcefilenode.SourceFileNode):
	def __init__(self,fname):
		super(UnknownFileNode,self).__init__(fname,pdmt.types.t_unknown)

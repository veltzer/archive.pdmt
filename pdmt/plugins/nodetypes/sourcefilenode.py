import pdmt.plugins.nodetypes.filenode # for NodeType
import os.path # for isfile

"""
this node represents an source file. Not just C. Any source file
"""

class NodeType(pdmt.plugins.nodetypes.filenode.NodeType):
	""" if a source file exists then it is upto date """
	""" question: why isn't a source file ALWAYS up to date?
	answer: what if the source file went missing? We want to trigger
	an error. Well - is it this methods part to check that the file
	exists ?!? I don't think so. This methods name is called "uptodate"
	and not "verify" or something... """
	def uptodate(self,todo):
		return True
#		return os.path.isfile(self.name)
	def canBuild(self):
		return False
	def clean(self):
		pass
	def build(self):
		raise ValueError('dont know how to build a source file')

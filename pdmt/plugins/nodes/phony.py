import pdmt.api # for NodeType

'''
This node represents a node which is not on disk or in any persistent storage.
It is usually used to connect other nodes.
like .PHONY in gmake...:)
'''

class NodeType(pdmt.api.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name=name, proto=proto)
		self.proto='phony'
	def needbuild(self,todo):
		return True
	def canBuild(self):
		return True
	def build(self):
		pass
	def canClean(self):
		return False
	def clean(self):
		pass

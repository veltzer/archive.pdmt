import pdmt.api # for NodeType

'''
This node represents an operation.
An operation is something that needs to run but does not depend on anything
'''

class NodeType(pdmt.api.NodeType):
	def __init__(self, type=None, name=None, proto=None):
		super().__init__(type=type, name=name, proto=proto)
		self.proto='operation'
	def uptodate(self,todo):
		return False
	def canBuild(self):
		return True
	def clean(self):
		pass

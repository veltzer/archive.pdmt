import pdmt.nodetypes.node
import os

class BuildNode(pdmt.nodetypes.node.Node):
	def canBuild(self):
		return True

import pdmt.plugins.nodetypes.buildnode # for NodeType
import pdmt.plugins.nodetypes.filenode # for NodeType
import pdmt.utils.fileops # for unlinksoft

"""
	a mixin class representing a node that can be built (not source)
"""
class NodeType(pdmt.plugins.nodetypes.filenode.NodeType,pdmt.plugins.nodetypes.buildnode.NodeType):
	def clean(self):
		pdmt.utils.fileops.unlinksoft(self.name)

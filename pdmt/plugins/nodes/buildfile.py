import pdmt.plugins.nodes.build # for NodeType
import pdmt.plugins.nodes.file # for NodeType
import pdmt.utils.fileops # for unlinksoft

"""
	a mixin class representing a node that can be built (not source)
"""
class NodeType(pdmt.plugins.nodes.file.NodeType,pdmt.plugins.nodes.build.NodeType):
	def clean(self):
		pdmt.utils.fileops.unlinksoft(self.name)

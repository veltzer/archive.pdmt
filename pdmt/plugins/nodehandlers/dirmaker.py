import pdmt.api
import pdmt.plugins.nodetypes.buildfilenode
import pdmt.utils.fileops

class NodeHandler(pdmt.api.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodeprebuild':
			return
		if not isinstance(node,pdmt.plugins.nodetypes.buildfilenode.NodeType):
			return
		pdmt.utils.fileops.mkdirparent_file(node.name)

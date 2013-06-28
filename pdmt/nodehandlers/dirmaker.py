import pdmt.nodehandler
import pdmt.nodetypes.buildfilenode
import pdmt.utils.fileops

class NodeHandler(pdmt.nodehandler.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodeprebuild':
			return
		if not isinstance(node,pdmt.nodetypes.buildfilenode.NodeType):
			return
		pdmt.utils.fileops.mkdirparent_file(node.m_fname)

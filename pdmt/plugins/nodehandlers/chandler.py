import pdmt.api
import pdmt.plugins.nodetypes.cfilenode
import pdmt.plugins.nodetypes.objectfilenode
import pdmt.config

class NodeHandler(pdmt.api.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmt.plugins.nodetypes.cfilenode.NodeType):
			return
		newname=node.m_fname[:node.m_fname.rfind(pdmt.config.ns_chandler.p_sourcefilesuffix)]+pdmt.config.ns_chandler.p_objectfilesuffix
		newnode=pdmt.plugins.nodetypes.objectfilenode.NodeType(newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))

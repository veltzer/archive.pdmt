import pdmt.nodehandler
import pdmt.nodetypes.cfilenode
import pdmt.nodetypes.objectfilenode
import pdmt.config

class NodeHandler(pdmt.nodehandler.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmt.nodetypes.cfilenode.NodeType):
			return
		newname=node.m_fname[:node.m_fname.rfind(pdmt.config.ns_chandler.p_sourcefilesuffix)]+pdmt.config.ns_chandler.p_objectfilesuffix
		newnode=pdmt.nodetypes.objectfilenode.NodeType(newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))

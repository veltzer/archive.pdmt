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
		newname=node.name[:node.name.rfind(pdmt.config.ns_chandler.p_sourcefilesuffix)]+pdmt.config.ns_chandler.p_objectfilesuffix
		newnode=pdmt.plugins.nodetypes.objectfilenode.NodeType(name=newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))

import pdmt.api # for Event.nodepostadd, NodeHandler
import pdmt.plugins.nodetypes.cfilenode # for NodeType
import pdmt.plugins.nodetypes.objectfilenode # for NodeType
import pdmt.config

class NodeHandler(pdmt.api.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!=pdmt.api.Event.nodepostadd:
			return
		if not isinstance(node,pdmt.plugins.nodetypes.cfilenode.NodeType):
			return
		newname=node.name[:node.name.rfind(pdmt.config.ns_chandler.p_sourcefilesuffix)]+pdmt.config.ns_chandler.p_objectfilesuffix
		newnode=pdmt.plugins.nodetypes.objectfilenode.NodeType(name=newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))

import pdmt.api # for Event.nodepostadd, NodeHandler
import pdmt.plugins.nodes.cfile # for NodeType
import pdmt.plugins.nodes.objectfile # for NodeType
import pdmt.config

class NodeHandler(pdmt.api.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!=pdmt.api.Event.nodepostadd:
			return
		if not isinstance(node,pdmt.plugins.nodes.cfile.NodeType):
			return
		newname=node.name[:node.name.rfind(pdmt.config.ns_chandler.p_sourcefilesuffix)]+pdmt.config.ns_chandler.p_objectfilesuffix
		newnode=pdmt.plugins.nodes.objectfile.NodeType(name=newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))

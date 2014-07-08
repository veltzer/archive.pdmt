import pdmt.api # for Event.nodepostadd, NodeHandler
import pdmt.plugins.nodes.makofile
import pdmt.plugins.nodes.makotfile
import pdmt.config
import os.path # for join, basename

class NodeHandler(pdmt.api.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!=pdmt.api.Event.nodepostadd:
			return
		if not isinstance(node,pdmt.plugins.nodes.makofile.NodeType):
			return
		name=node.name[:node.name.rfind(pdmt.config.ns_makohandler.p_sourcefilesuffix)]
		newname=os.path.join(pdmt.config.ns_makohandler.p_targetdir,os.path.basename(name))
		newnode=pdmt.plugins.nodes.makotfile.NodeType(name=newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))

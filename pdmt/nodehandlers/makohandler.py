import pdmt.nodetypes.makofilenode
import pdmt.nodetypes.unknownfilenode

import pdmt.config
import config

class MakoHandler:
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmt.nodetypes.makofilenode.MakoFileNode):
			return
		newname=node.fname[:node.fname.rfind(config.ns_makohandler.p_sourcefilesuffix)]
		newnode=pdmt.nodetypes.unknownfilenode.UnknownFileNode(newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))

import pdmt.nodetypes.makofilenode
import pdmt.nodetypes.makotfilenode

import pdmt.config
import config

import os

class MakoHandler:
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmt.nodetypes.makofilenode.MakoFileNode):
			return
		name=node.fname[:node.fname.rfind(config.ns_makohandler.p_sourcefilesuffix)]
		newname=os.path.join(config.ns_makohandler.p_targetdir,os.path.basename(name))
		#newname=node.fname[:node.fname.rfind(config.ns_makohandler.p_sourcefilesuffix)]
		newnode=pdmt.nodetypes.makotfilenode.MakotFileNode(newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))
